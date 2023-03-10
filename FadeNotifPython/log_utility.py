# coding=utf-8

import threading
import utilities
from datetime import datetime

# trial log

TIMING_KEY_TRIAL = "trial"
TIMING_KEY_GLOBAL_TIME = "global_time"
TIMING_KEY_TASK_TIME = "task_time"


def _get_timing_log_file(participant, session):
    return f'data/{participant}/{participant}_{session}_timing.csv'


def log_timing(participant, session, trial, global_time, task_time):
    file_name = _get_timing_log_file(participant, session)

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{TIMING_KEY_TRIAL},{TIMING_KEY_GLOBAL_TIME},{TIMING_KEY_TASK_TIME}\n')

    utilities.append_data(file_name, f'{trial},{global_time},{task_time}\n')


def log_all_timing(participant, session, data):
    file_name = _get_timing_log_file(participant, session)

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{TIMING_KEY_TRIAL},{TIMING_KEY_GLOBAL_TIME},{TIMING_KEY_TASK_TIME}\n')

    utilities.append_data(file_name, data)


def log_timing_threaded(participant, session, trial, global_time, task_time):
    threading.Thread(target=log_timing,
                     args=(participant, str(int(session)), trial, global_time, task_time)).start()


# notification log
NOTIFICATION_KEY_ID = "id"
NOTIFICATION_KEY_SEND_START_TIME = "send_start_time"
NOTIFICATION_KEY_SEND_COMPLETE_TIME = "send_complete_time"
NOTIFICATION_KEY_DATA = "data"


def _get_notification_log_file(participant, session):
    return f'data/{participant}/{participant}_{session}_notification_info.csv'


def log_notification_info(participant, session, notification):
    file_name = _get_notification_log_file(participant, session)

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{NOTIFICATION_KEY_ID},{NOTIFICATION_KEY_SEND_START_TIME},{NOTIFICATION_KEY_SEND_COMPLETE_TIME},{NOTIFICATION_KEY_DATA}\n')

    notification_info = '"' + f'{notification}'.replace('"', '""') + '"'
    utilities.append_data(file_name,
                          f'{notification[NOTIFICATION_KEY_ID]},{notification[NOTIFICATION_KEY_SEND_START_TIME]},{notification[NOTIFICATION_KEY_SEND_COMPLETE_TIME]},{notification_info}\n')


# participant log

PARTICIPANT_KEY_ID = "id"
PARTICIPANT_KEY_SESSION = "session"
PARTICIPANT_KEY_TASK_TYPE = "task"
PARTICIPANT_KEY_TASK_LOCATION = "location"
PARTICIPANT_KEY_TASK_MOBILITY = "mobility"
PARTICIPANT_KEY_NOTIFICATION_TYPE = "notification"
PARTICIPANT_KEY_TIME = "time"


def _get_participant_log_file(participant):
    return f'data/{participant}/{participant}_config.csv'


def log_participant_info(participant, session, task_type, task_location, task_mobility,
                         notification_type):
    file_name = _get_participant_log_file(participant)
    print(
        f'Participant info: {participant}, session: {session}, task: {task_type}, location: {task_location}, mobility: {task_mobility}, notification_type: {notification_type}')

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{PARTICIPANT_KEY_ID},{PARTICIPANT_KEY_SESSION},{PARTICIPANT_KEY_TASK_TYPE},{PARTICIPANT_KEY_TASK_LOCATION},{PARTICIPANT_KEY_TASK_MOBILITY},{PARTICIPANT_KEY_NOTIFICATION_TYPE},{PARTICIPANT_KEY_TIME}\n')

    utilities.append_data(file_name,
                          f'{participant},{session},{task_type},{task_location},{task_mobility},{notification_type},{datetime.now()}\n')


# passage log
PASSAGE_KEY_ID = "id"
PASSAGE_KEY_TEXT = "text"
PASSAGE_KEY_SUBSTITUTES = "substitutes"
PASSAGE_KEY_DURATION = "duration"


def _get_passage_log_file(participant, session):
    return f'data/{participant}/{participant}_{session}_passage_info.csv'


def log_passage_info(participant, session, passage):
    file_name = _get_passage_log_file(participant, session)

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{PASSAGE_KEY_ID},{PASSAGE_KEY_TEXT},{PASSAGE_KEY_SUBSTITUTES},{PASSAGE_KEY_DURATION}\n')

    passage_content = passage[PASSAGE_KEY_TEXT].replace('"', '""')

    utilities.append_data(file_name,
                          f'{passage[PASSAGE_KEY_ID]},"{passage_content}","{passage[PASSAGE_KEY_SUBSTITUTES]}",{passage[PASSAGE_KEY_DURATION]}\n')
