# coding=utf-8

# command format: python3 process_raw_data.py -p <PARTICIPANT_ID> -s <SESSION_ID>

import participant_config
import numpy as np
import optparse
import pandas as pd
import stimuli_generation
import utilities

# data related to vigilance task
STIMULI_DURATION_MS = stimuli_generation.IMAGE_DURATION_MS  # 625
HIT_TOLERANCE_DURATION_MS = 2000

HIT_TOLERANCE_INDICES = HIT_TOLERANCE_DURATION_MS // STIMULI_DURATION_MS  # i.e.  3 * 625 ms ~ 1900 ms, 625 ms is the stimuli duration

CLICK_EXPECTED_IMAGE_IDS = stimuli_generation.get_stimuli_image_ids()
NOISE_STIMULI_TYPES = stimuli_generation.get_noise_stimuli()
NOISE_STIMULI_DURATION_INDICES = stimuli_generation.get_noise_stimuli_size()


# input: data directory
def get_data_directory(participant):
    return f'data/{participant}'


# input: related to stimuli response
def get_stimuli_file_name_prefix(participant, session):
    return f'{participant}_{session}_tasks_psychopy'


COLUMN_STIMULI_TYPE = 'stimuli_type'
COLUMN_STIMULI_ID = 'stimuli_id'
COLUMN_STIMULI_IMAGE_ID = 'image_id'
COLUMN_STIMULI_TRIAL_ID = 'trials_v.thisRepN'
COLUMN_STIMULI_STIMULI_TIME = 'im_v.started'
COLUMN_STIMULI_CLICK_TIMES = 'mouse_v.time'

COLUMN_STIMULI_READING_REACTION_TIME = 'key_resp.rt'

COLUMN_STIMULI_RECOGNITION_INDEX = 'form_recog.index'
COLUMN_STIMULI_RECOGNITION_TEXT = 'form_recog.itemText'
COLUMN_STIMULI_RECOGNITION_ANSWER = 'form_recog.response'


# input: related to notification stimuli
def get_notification_info_file_name_prefix(participant, session):
    return f'{participant}_{session}_notification_info'


COLUMN_NOTIFICATION_ID = 'id'
COLUMN_NOTIFICATION_SEND_START_TIME = 'send_start_time'
COLUMN_NOTIFICATION_SEND_COMPLETE_TIME = 'send_complete_time'


# input: related to timing info
def get_timing_info_file_name_prefix(participant, session):
    return f'{participant}_{session}_timing'


COLUMN_TIMING_TRIAL = 'trial'
COLUMN_TIMING_GLOBAL_TIME = 'global_time'
COLUMN_TIMING_TASK_TIME = 'task_time'

# input: related to passage
MIN_SUBSTITUTE_COUNT = 10


def get_passage_info_file_name_prefix(participant, session):
    return f'{participant}_{session}_passage_info'


COLUMN_PASSAGE_KEY_ID = "id"
COLUMN_PASSAGE_KEY_TEXT = "text"
COLUMN_PASSAGE_KEY_SUBSTITUTES = "substitutes"
COLUMN_PASSAGE_KEY_DURATION = "duration"


# output: converted files
def get_vigilance_output_file_name_format(participant, session):
    return f'data/{participant}/{participant}_{session}_vigilance.csv'


def get_summary_output_file_name_format(participant):
    return f'data/{participant}/{participant}_summary.csv'


def read_csv_file_with_header(csv_file):
    return pd.read_csv(csv_file, header=0)


def get_array_without_none(array):
    return [item for item in array if item is not None]


# return data_frame from stimuli_response file
def get_stimuli_response_data_frame(participant, session):
    data_directory = get_data_directory(participant)
    stimuli_response_files = utilities.read_file_names(data_directory, '.csv',
                                                       get_stimuli_file_name_prefix(
                                                           participant, session))
    return read_csv_file_with_header(stimuli_response_files[0])


# return notification_count, notification_ids[], notification_sent_time[]
def get_notification_info(participant, session):
    # notification stimuli data
    data_directory = get_data_directory(participant)
    notification_stimuli_files = utilities.read_file_names(data_directory, '.csv',
                                                           get_notification_info_file_name_prefix(
                                                               participant, session))
    notification_count = 0
    notification_sent_time = []
    notification_ids = []
    if len(notification_stimuli_files) > 0:  # if there is any data file
        data_frame_notifications = read_csv_file_with_header(notification_stimuli_files[0])
        notification_count = data_frame_notifications.shape[0]
        notification_sent_time = np.array(
            data_frame_notifications[COLUMN_NOTIFICATION_SEND_START_TIME])
        notification_ids = np.array(
            data_frame_notifications[COLUMN_NOTIFICATION_ID])
    return notification_count, notification_ids, notification_sent_time


# create the processed csv file and return {"duration":<SECONDS>, "notification_count":<>, "stimuli_count":<RECTANGLE_OCCURRENCE>}
def process_vigilance_data(participant, session):
    # image stimuli and click data
    data_frame_image_stimuli_response = get_stimuli_response_data_frame(participant, session)
    # print(data_frame_image_stimuli_response.shape)

    ori_round = data_frame_image_stimuli_response[COLUMN_STIMULI_TRIAL_ID]
    row_count_on_vigilance = sum(ori_round.notna())
    ori_round = ori_round[:row_count_on_vigilance]  # filter the responses related to the vigilance
    ori_image_stimuli = data_frame_image_stimuli_response[COLUMN_STIMULI_IMAGE_ID][
                        :row_count_on_vigilance]
    ori_stimuli_type = data_frame_image_stimuli_response[COLUMN_STIMULI_TYPE][
                       :row_count_on_vigilance]
    # ori_click_times are w.r.t task
    ori_image_stimuli_time = np.array(
        data_frame_image_stimuli_response[COLUMN_STIMULI_STIMULI_TIME][:row_count_on_vigilance])
    # click_times are w.r.t global clock
    ori_click_times = data_frame_image_stimuli_response[COLUMN_STIMULI_CLICK_TIMES][
                      :row_count_on_vigilance]
    # print(ori_click_times)

    click_times = [float(str_time.replace('[', '').replace(']', '')) for str_time in ori_click_times
                   if str_time != '[]' and pd.notna(str_time)]
    # print(click_times)

    # timing data for synchronization
    timing_info_files = utilities.read_file_names(get_data_directory(participant), '.csv',
                                                  get_timing_info_file_name_prefix(participant,
                                                                                   session))
    data_frame_timing_info = read_csv_file_with_header(timing_info_files[0])
    experiment_time_shift = np.array(data_frame_timing_info[COLUMN_TIMING_TASK_TIME]) - np.array(
        data_frame_timing_info[COLUMN_TIMING_GLOBAL_TIME])  # 1D array for each trial
    # print(data_frame_timing_info, experiment_time_shift)

    # time shift for synchronization
    image_stimuli_time = ori_image_stimuli_time.copy()
    if len(experiment_time_shift) > 1:
        image_stimuli_time -= experiment_time_shift[1:]
    else:
        image_stimuli_time -= experiment_time_shift[0]
        print(' ** Only 1 values found for time syncing')
    # print(image_stimuli_time)

    # notification info
    notification_count, _, notification_stimuli_time = get_notification_info(participant, session)

    # print(f'click_times:{click_times}, image_stimuli_time: {image_stimuli_time}, notification_count: {notification_count}, notification_stimuli_time: {notification_stimuli_time}')

    mapped_click_time = []
    click_time_count = len(click_times)
    index_click_time = 0

    mapped_notification_time = []
    index_notification_time = 0

    # align stimuli, click and notification time
    for image_time in image_stimuli_time:
        if index_click_time < click_time_count and click_times[index_click_time] < image_time:
            mapped_click_time.append(click_times[index_click_time])
            index_click_time += 1
        else:
            mapped_click_time.append(None)

        if index_notification_time < notification_count and notification_stimuli_time[
            index_notification_time] < image_time:
            mapped_notification_time.append(notification_stimuli_time[index_notification_time])
            index_notification_time += 1
        else:
            mapped_notification_time.append(None)

        # if index_click_time >= click_time_count and index_notification_time >= notification_count:
        #     break

    # print(mapped_click_time, mapped_notification_time)

    # calculate hit, miss, false alarm, reaction time
    hit = []
    miss = []
    false_alarm = []
    correct_rejection = []
    reaction_time = []

    prev_stimuli_type = None

    total_stimuli_count = len(image_stimuli_time)
    for index in range(total_stimuli_count):
        # hit or miss
        if ori_image_stimuli[index] in CLICK_EXPECTED_IMAGE_IDS:
            hit_click_indices = [click_index for click_index in
                                 range(index,
                                       min(index + HIT_TOLERANCE_INDICES, total_stimuli_count))
                                 if mapped_click_time[click_index] is not None]
            if len(hit_click_indices) > 0:
                hit.append(1)
                miss.append(None)
                rt_instance = mapped_click_time[hit_click_indices[0]] - image_stimuli_time[index]
                if rt_instance < 0:
                    print(f' *** Negative reaction time: {rt_instance}, index: {index}')
                reaction_time.append(abs(rt_instance))
            else:
                hit.append(None)
                miss.append(1)
                reaction_time.append(None)
        else:
            hit.append(None)
            miss.append(None)
            reaction_time.append(None)

        # false alarm
        if mapped_click_time[index] is not None:
            hit_stimuli_indices = [stimuli_index for stimuli_index in
                                   range(index, max(0, index - HIT_TOLERANCE_INDICES), -1) if
                                   ori_image_stimuli[stimuli_index] in CLICK_EXPECTED_IMAGE_IDS]
            if len(hit_stimuli_indices) > 0:
                false_alarm.append(None)
            else:
                false_alarm.append(1)
        else:
            false_alarm.append(None)

        # correct rejection
        current_stimuli_type = ori_stimuli_type[index]
        if current_stimuli_type != prev_stimuli_type and current_stimuli_type in NOISE_STIMULI_TYPES:
            clicks_during_noise = [click_index for click_index in range(index, min(
                index + NOISE_STIMULI_DURATION_INDICES, total_stimuli_count)) if
                                   mapped_click_time[click_index] is not None]
            if len(clicks_during_noise) == 0:
                correct_rejection.append(1)
            else:
                correct_rejection.append(0)
        else:
            correct_rejection.append(None)

        prev_stimuli_type = current_stimuli_type

    # calculate total hit, miss, false alarm, (average) reaction time during notification
    hit_sum_notification = [None] * total_stimuli_count
    miss_sum_notification = [None] * total_stimuli_count
    false_alarm_sum_notification = [None] * total_stimuli_count
    correct_rejection_sum_notification = [None] * total_stimuli_count
    reaction_time_avg_notification = [None] * total_stimuli_count

    notification_duration_millis = participant_config.get_notification_duration(participant,
                                                                                session)
    notification_duration_indices = notification_duration_millis // STIMULI_DURATION_MS  # i.e. 17 * 625 ~ 10 s

    notification_indices = [index for index in range(total_stimuli_count) if
                            mapped_notification_time[index] is not None]
    for notification_start_index in notification_indices:
        notification_end_index = min(notification_start_index + notification_duration_indices,
                                     total_stimuli_count)
        hit_sum_notification[notification_start_index] = np.sum(get_array_without_none(
            hit[notification_start_index: notification_end_index]))
        miss_sum_notification[notification_start_index] = np.sum(get_array_without_none(
            miss[notification_start_index: notification_end_index]))
        false_alarm_sum_notification[notification_start_index] = np.sum(get_array_without_none(
            false_alarm[notification_start_index: notification_end_index]))
        reaction_time_avg_notification[notification_start_index] = np.sum(get_array_without_none(
            correct_rejection[notification_start_index: notification_end_index]))
        reaction_time_avg_notification[notification_start_index] = np.mean(get_array_without_none(
            reaction_time[notification_start_index: notification_end_index]))

        # print(hit_sum_notification[notification_start_index],
        #       miss_sum_notification[notification_start_index],
        #       false_alarm_sum_notification[notification_start_index],
        #       reaction_time_avg_notification[notification_start_index],
        #       reaction_time_avg_notification[notification_start_index: notification_end_index])

    csv_data = {'round': ori_round,
                'type': ori_stimuli_type,
                'image': ori_image_stimuli,
                'start_time': image_stimuli_time,
                'click_time': mapped_click_time,
                'notification_time': mapped_notification_time,
                'hit': hit,
                'miss': miss,
                'false_alarm': false_alarm,
                'correct_rejection': correct_rejection,
                'reaction_time': reaction_time,
                'hit-sum-notification': hit_sum_notification,
                'miss-sum-notification': miss_sum_notification,
                'false_alarm-sum-notification': false_alarm_sum_notification,
                'correct_rejection-sum-notification': correct_rejection_sum_notification,
                'reaction_time-avg-notification': reaction_time_avg_notification,
                'ori.stimuli_time': ori_image_stimuli_time,
                'ori.click_time': ori_click_times}
    # print(csv_data)
    converted_file_name = get_vigilance_output_file_name_format(participant, session)
    pd.DataFrame(data=csv_data).to_csv(converted_file_name)
    print(f'\nVigilance data is written to [{converted_file_name}]')

    tot_hit, tot_miss, tot_false_alarm, tot_correct_reject = get_stats(csv_data)
    print_stats(click_time_count, tot_hit, tot_miss, tot_false_alarm, tot_correct_reject)

    result = {
        "duration": row_count_on_vigilance * STIMULI_DURATION_MS / 1000,
        "stimuli_count": tot_hit + tot_miss,
    }
    return result


def get_stats(csv_data):
    total_hit = np.sum(get_array_without_none(csv_data["hit"]))
    total_miss = np.sum(get_array_without_none(csv_data["miss"]))
    total_false_alarm = np.sum(get_array_without_none(csv_data["false_alarm"]))
    total_correct_reject = np.sum(get_array_without_none(csv_data["correct_rejection"]))

    return total_hit, total_miss, total_false_alarm, total_correct_reject


def print_stats(click_count, tot_hit, tot_miss, tot_false_alarm, tot_correct_reject):
    print(f'\t[Clicks: {click_count}] '
          f'Hit: {tot_hit}, '
          f'Miss: {tot_miss}, '
          f'False Alarm: {tot_false_alarm}, '
          f'Correct Rejection: {tot_correct_reject}'
          f'\n')


# return {"duration":<SECONDS>, "stimuli_count":<SUBSTITUTION_WORD_COUNT>}
def process_reading_data(participant, session):
    # passage info
    data_directory = get_data_directory(participant)
    passage_info_files = utilities.read_file_names(data_directory, '.csv',
                                                   get_passage_info_file_name_prefix(
                                                       participant, session))

    data_frame_passage_info = read_csv_file_with_header(passage_info_files[0])
    ori_substitutes = data_frame_passage_info[COLUMN_PASSAGE_KEY_SUBSTITUTES]
    ori_ids = data_frame_passage_info[COLUMN_PASSAGE_KEY_ID]

    passage_ids = [int(id) for id in ori_ids if pd.notna(id)]
    # print(passage_ids)

    substitutes_list = [
        str_sub.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split(",") for
        str_sub in ori_substitutes
        if str_sub != '[]' and pd.notna(str_sub)]
    # print(substitutes_list)
    # e.g., [['11', '1', 'rite->write', '2', 'cool->school', 'teaser->teacher', '2', 'clear->clever', 'lawn->learn', ...]]
    if len(substitutes_list) != 1 or len(passage_ids) > 1:
        print("\n\t Error: passage info has more than 1 passage")

    substitution_count = int(substitutes_list[0][0])
    if substitution_count < MIN_SUBSTITUTE_COUNT:
        print(f'\n\t Error: passage info less than {MIN_SUBSTITUTE_COUNT} substitutes')

    # read reading time from stimuli file
    stimuli_response_data_frame = get_stimuli_response_data_frame(participant, session)
    data_frame_indices = stimuli_response_data_frame[COLUMN_STIMULI_READING_REACTION_TIME].notna()
    ori_reaction_times = stimuli_response_data_frame[COLUMN_STIMULI_READING_REACTION_TIME][
        data_frame_indices]

    reaction_times = [float(str_time.replace('[', '').replace(']', '')) for str_time in
                      ori_reaction_times
                      if str_time != '[]' and pd.notna(str_time)]
    # print(reaction_times)
    if len(reaction_times) != 1:
        print("\n\t Error: reading has multiple reaction times")

    result = {
        "duration": reaction_times[0],
        "stimuli_count": substitution_count,
        "task_id": passage_ids[0],
    }
    # print(result)
    return result


# return {"notification_count":<NUMBER>, "recognition_count_correct":<NUMBER>, "recognition_count_incorrect": <NUMBER>}
def process_recognition_data(participant, session):
    notification_count, notification_ids, _ = get_notification_info(participant, session)

    if notification_count <= 0:
        return {
            "notification_count": 0,
            "recognition_count_correct": "",
            "recognition_count_incorrect": "",
        }

    stimuli_response_data_frame = get_stimuli_response_data_frame(participant, session)

    data_frame_indices = stimuli_response_data_frame[COLUMN_STIMULI_RECOGNITION_INDEX].notna()
    ori_index_answer = stimuli_response_data_frame[
        [COLUMN_STIMULI_RECOGNITION_INDEX, COLUMN_STIMULI_RECOGNITION_ANSWER]][data_frame_indices]

    correct_hit_mask = (ori_index_answer[COLUMN_STIMULI_RECOGNITION_INDEX] < 1000) & (
            ori_index_answer[COLUMN_STIMULI_RECOGNITION_ANSWER] == 'Yes')
    correct_correct_reject_mask = (ori_index_answer[COLUMN_STIMULI_RECOGNITION_INDEX] >= 1000) & (
            ori_index_answer[COLUMN_STIMULI_RECOGNITION_ANSWER] == 'No')
    correct_mask = (correct_hit_mask | correct_correct_reject_mask)

    correct_count = sum(correct_mask)
    total_responses = sum(data_frame_indices)

    result = {
        "notification_count": notification_count,
        "recognition_count_correct": correct_count,
        "recognition_count_incorrect": total_responses - correct_count,
    }
    # print(result)
    return result


def process_participant_session_data(participant, session):
    print(f'\nParticipant: {participant}, session: {session}')

    task = participant_config.get_task_type(participant, session)
    location = participant_config.get_task_location(participant, session)
    mobility = participant_config.get_task_mobility(participant, session)
    expected_task_duration = participant_config.get_task_duration(participant, session)
    expected_notification_count = participant_config.get_notification_count(participant, session)
    expected_recognition_count = participant_config.get_notification_recognition_count(participant,
                                                                                       session)
    notification_duration = participant_config.get_notification_duration(participant, session)
    notification_config = participant_config.get_notification_config(participant, session)

    if task != participant_config.TASK_TYPE_VIGILANCE and task != participant_config.TASK_TYPE_PROOFREADING:
        print("Unsupported task")
        return

    task_result = {}
    if task == participant_config.TASK_TYPE_VIGILANCE:
        task_result = process_vigilance_data(participant, session)
    if task == participant_config.TASK_TYPE_PROOFREADING:
        task_result = process_reading_data(participant, session)

    recognition_result = process_recognition_data(participant, session)

    file_name = get_summary_output_file_name_format(participant)
    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{"Participant"},{"Session"},'
                              f'{"Task"},{"Location"},{"Mobility"},{"ExpectedTaskDuration"},'
                              f'{"TaskDuration"},{"TaskId"},{"StimuliCount"},'
                              f'{"ExpectedNotification#"},{"ExpectedRecognition#"},'
                              f'{"Notification#"},{"RecognitionCorrect#"},{"RecognitionIncorrect#"},'
                              f'{"NotificationDuration"},'
                              f'{"DisplayType,SlideDown,SlideUp,GradEntry,GradExit"}\n')

    utilities.append_data(file_name,
                          f'{participant},{session},'
                          f'{task},{location},{mobility},{expected_task_duration},'
                          f'{task_result["duration"]},{_get_task_id(task_result)},{task_result["stimuli_count"]},'
                          f'{expected_notification_count},{expected_recognition_count},'
                          f'{recognition_result["notification_count"]},{recognition_result["recognition_count_correct"]},{recognition_result["recognition_count_incorrect"]},'
                          f'{notification_duration},'
                          f'{notification_config}\n')

    print(f'Session {session} data is added to [{file_name}]\n')


def _get_task_id(task_result):
    if task_result is None or task_result.get('task_id') is None:
        return ''
    return task_result.get('task_id')


def get_testing_sessions(participant):
    sessions = participant_config.get_all_sessions(participant)
    return [x for x in sessions if not participant_config.is_training(participant, x)]


def process_participant_data(participant):
    sessions = get_testing_sessions(participant)

    for session in sessions:
        process_participant_session_data(participant, session)


# command line interface
parser = optparse.OptionParser()
parser.add_option("-p", "--participant", dest="participant")
parser.add_option("-s", "--session", dest="session")

options, args = parser.parse_args()

# print options
# print args
_participant = options.participant
_session = options.session

if _session is None:
    process_participant_data(_participant)
else:
    process_participant_session_data(_participant, _session)
