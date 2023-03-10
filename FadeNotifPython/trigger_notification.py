# coding=utf-8

import display_formatter
import notification_data
import device_driver
import log_utility
import participant_config
import pandas as pd

import sys
import threading
import time
import traceback
import utilities
from random import randint
from random import sample
from random import shuffle

START_NOTIFICATION_GAP_SECONDS = 2 + 4
MIN_NOTIFICATION_GAP_SECONDS = 4
MAX_NOTIFICATION_GAP_SECONDS = 10

NOTIFICATION_KEY_SEND_START_TIME = "send_start_time"
NOTIFICATION_KEY_SEND_COMPLETE_TIME = "send_complete_time"
NOTIFICATION_KEY_SEND_SUCCESS = "send_success"


# return the 'id' (or 100 * 'id') of notification if it matches 'title' (or 'alternative'), else 0
def _get_index_id(title_or_alternative, notification_list):
    for notification in notification_list:
        if notification['title'] == title_or_alternative:
            return notification['id']
        elif notification['alternative'] == title_or_alternative:
            return notification['id'] * 100
    return 0


# Assume the notification has 'id', 'title', and 'alternative' fields
def _set_notification_recognition_questions(notification_list, notification_recognition_count):
    all_possible_choices = [notification['title'] for notification in notification_list] + [
        notification['alternative'] for notification in notification_list]
    shuffle(all_possible_choices)

    selected_choices = sample(all_possible_choices, notification_recognition_count)
    notification_recognition_options = ['Yes,No'] * notification_recognition_count

    # This follows the format of PsychoPy Form component (https://www.psychopy.org/builder/components/form.html)
    stimuli_csv_data = {
        'index': [_get_index_id(x, notification_list) for x in selected_choices],
        'itemText': selected_choices,
        'options': notification_recognition_options,
        'type': ['radio'] * notification_recognition_count
    }
    csv_file_name = 'stimuli/recognition_stimuli.csv'
    pd.DataFrame(data=stimuli_csv_data).to_csv(csv_file_name, mode='w', index=False)
    print('Generated recognition stimuli csv: ', csv_file_name)


def _set_empty_notification_recognition_questions():
    utilities.write_data('stimuli/recognition_stimuli.csv', 'index,itemText,options,type')


def get_notification_list(participant, session):
    notification_type = participant_config.get_notification_type(participant, session)
    notification_count = participant_config.get_notification_count(participant, session)
    notification_config = participant_config.get_notification_config(participant, session)
    notification_duration_millis = participant_config.get_notification_duration(participant,
                                                                                session)
    notification_recognition_count = participant_config.get_notification_recognition_count(
        participant, session)

    print(
        f'Setting notifications:: participant: {participant}, session: {session}, type:{notification_type}. count: {notification_count}')

    if notification_count <= 0:
        print('No notifications!')
        _set_empty_notification_recognition_questions()
        return []

    raw_notification_list = notification_data.get_next_notifications(notification_type,
                                                                     notification_count,
                                                                     participant)
    # set the questions for recognition (Note: Notifications should have  'id', 'title', and 'alternative' keys)
    _set_notification_recognition_questions(raw_notification_list, notification_recognition_count)

    notification_list = [
        display_formatter.get_notification(notification_content, 0, notification_duration_millis,
                                           notification_config) for notification_content in
        raw_notification_list]

    return notification_list


# Trigger notifications based on participant and session
# global_clock: use `getTime()` method to log time
def trigger_notification_randomly(participant, session, notification_list, global_clock):
    global flag_is_running

    print(f'Start sending notifications:: participant: {participant}, session: {session}')

    notification_count = len(notification_list)
    if notification_count <= 0:
        print('No notifications to trigger')
        return

    # distribute notification during task
    task_duration_seconds = participant_config.get_task_duration(participant, session)
    notification_duration_millis = notification_list[0][
        "duration"]  # each notification has a duration

    min_notification_gap_seconds, max_notification_gap_seconds = _get_notification_gap_range(
        notification_count, notification_duration_millis, task_duration_seconds)
    notification_gaps_seconds = _get_notification_gaps(notification_count,
                                                       min_notification_gap_seconds,
                                                       max_notification_gap_seconds)
    print(
        f'Notification duration: {notification_duration_millis / 1000}, min gap: {min_notification_gap_seconds}, max gap: {max_notification_gap_seconds}')

    current_time = time.time()  # in seconds
    sent_time = 0
    # first notification scheduling
    scheduled_send_time = current_time + START_NOTIFICATION_GAP_SECONDS + notification_gaps_seconds[
        0]

    notification_sent_count = 0
    while notification_sent_count < notification_count and flag_is_running:

        current_time = time.time()

        if current_time > scheduled_send_time:
            # send notification
            notification = notification_list[notification_sent_count]
            notification[NOTIFICATION_KEY_SEND_START_TIME] = global_clock.getTime()

            print(
                f'Sending notification:: count: {notification_sent_count + 1}, id: {notification["id"]}')
            success = device_driver.send_notification_data(notification)

            notification[NOTIFICATION_KEY_SEND_COMPLETE_TIME] = global_clock.getTime()
            notification[NOTIFICATION_KEY_SEND_SUCCESS] = success
            log_utility.log_notification_info(participant, session, notification)

            current_time = time.time()
            sent_time = current_time

            # next notification scheduling
            notification_sent_count += 1
            notification_gap = notification_gaps_seconds[notification_sent_count]
            scheduled_send_time = sent_time + notification_duration_millis / 1000 + notification_gap

            print(f'notification gap: {notification_gap}')

        # if current_time > sent_time + notification_duration_millis/1000:
        #     # clear the notification
        #     device_driver.clear_notification_data()
        #     sent_time = scheduled_send_time

        # sleep
        utilities.sleep_seconds(0.1)

    print(
        f'Stop sending notifications:: participant: {participant}, session: {session}, sent %: {notification_sent_count}/{notification_count}')

    # if not flag_is_running:
    #     device_driver.clear_notification_data()

    flag_is_running = False


# return min and max gap in seconds
def _get_notification_gap_range(notification_count, notification_duration_millis,
                                task_duration_seconds):
    max_notification_gap_seconds = int(
        (task_duration_seconds / notification_count - notification_duration_millis / 1000)) + 1
    max_notification_gap_seconds = min(max_notification_gap_seconds, MAX_NOTIFICATION_GAP_SECONDS)
    min_notification_gap_seconds = max(max_notification_gap_seconds // 4,
                                       MIN_NOTIFICATION_GAP_SECONDS)
    # min_notification_gap_seconds = MIN_NOTIFICATION_GAP_SECONDS
    # max_notification_gap_seconds = MAX_NOTIFICATION_GAP_SECONDS
    return min_notification_gap_seconds, max_notification_gap_seconds


# return random gaps with of (notification_count + 1)
def _get_notification_gaps(notification_count, min_notification_gap_seconds,
                           max_notification_gap_seconds):
    # select (notification_count) gaps randomly
    notification_gaps_seconds = []
    notification_gap_range = range(min_notification_gap_seconds, max_notification_gap_seconds + 1)
    count_gap_range = len(notification_gap_range)
    if notification_count < count_gap_range:
        notification_gaps_seconds = sample(notification_gap_range, notification_count)
    else:
        rounds = notification_count // count_gap_range
        for _ in range(rounds):
            notification_gaps_seconds += sample(notification_gap_range, count_gap_range)
        notification_gaps_seconds += sample(notification_gap_range,
                                            notification_count - rounds * count_gap_range)
    # add extra gap
    notification_gaps_seconds += sample(notification_gap_range, 1)
    return notification_gaps_seconds


def trigger_notification_randomly_with_exception(participant, session, notification_list,
                                                 global_clock):
    try:
        trigger_notification_randomly(participant, session, notification_list, global_clock)
    except Exception:
        print("Unhandled exception")
        traceback.print_exc(file=sys.stdout)


flag_is_running = False


def trigger_notification_randomly_threaded(participant, session, notification_list, global_clock):
    global flag_is_running

    if not flag_is_running:
        flag_is_running = True
        threading.Thread(target=trigger_notification_randomly_with_exception, args=(
            participant, str(int(session)), notification_list, global_clock)).start()
        print("Starting triggering!")
    else:
        print("Triggering is running!")


def cancel_notification_trigger():
    global flag_is_running

    flag_is_running = False


# trigger_notification_randomly("p00", '3', get_notification_list("p00", '3'), None)
