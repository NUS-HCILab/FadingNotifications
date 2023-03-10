# coding=utf-8

EXPECTED_READING_TASK_DURATION_SECONDS = 220

EXPECTED_VIGILANCE_TASK_DURATION_SECONDS = 225

TASK_VIGILANCE_NOTIFICATION_COUNT = 14
TASK_VIGILANCE_RECOGNITION_COUNT = 20
TASK_PROOFREADING_NOTIFICATION_COUNT = 12
TASK_PROOFREADING_RECOGNITION_COUNT = 16

NOTIFICATION_DURATION_MILLIS = 10000

TASK_TYPE_VIGILANCE = 'vigilance'
TASK_TYPE_PROOFREADING = 'reading'

TASK_LOCATION_DESKTOP = 'desktop'
TASK_LOCATION_GLASS = 'glass'

MOBILITY_SITTING = 'sitting'
MOBILITY_WALKING = 'walking'


def is_training(participant, session):
    return int(session) < 0


def get_all_sessions(participant):
    session_data = CONFIG[participant]
    return list(session_data.keys())


def get_task_type(participant, session):
    return CONFIG[participant][session]['task']['type']


def get_task_mobility(participant, session):
    return CONFIG[participant][session]['task']['mobility']


# return in seconds
def get_task_duration(participant, session):
    return CONFIG[participant][session]['task']['duration']


def get_task_location(participant, session):
    return CONFIG[participant][session]['task']['location']


def get_notification_type(participant, session):
    return CONFIG[participant][session]['notification']['type']


def get_notification_count(participant, session):
    return CONFIG[participant][session]['notification']['count']


def get_notification_recognition_count(participant, session):
    return CONFIG[participant][session]['notification']['recognition_count']


# return in millis
def get_notification_duration(participant, session):
    return CONFIG[participant][session]['notification']['duration']


def get_notification_config(participant, session):
    notification_config_object = CONFIG[participant][session]['notification']
    return _get_notification_config(notification_config_object)


def _get_notification_config(notification_config_object):
    # FORMAT: PROGRESSIVE_WITH_<TYPE>, <slide_appear_millis>, <slide_disappear_millis>, <appear_intensity_millis>, <disappear_intensity_millis>, YYY
    return f'{notification_config_object["display_type"]},' \
           f'{notification_config_object["slide_down"]},' \
           f'{notification_config_object["slide_up"]},' \
           f'{notification_config_object["gradual_entry"]},' \
           f'{notification_config_object["gradual_exit"]}'


CONFIG = {
    "p00": {
        '-1': {
            'task': {
                'type': TASK_TYPE_VIGILANCE,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 340,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 340,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 340,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '0': {
            'task': {
                'type': TASK_TYPE_VIGILANCE,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 3,
                'recognition_count': 5,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 340,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 3,
                'recognition_count': 5,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 340,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 3,
                'recognition_count': 5,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 340,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },

        '3': {
            'task': {
                'type': TASK_TYPE_VIGILANCE,
                'duration': EXPECTED_VIGILANCE_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 12,
                'recognition_count': 16,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
    },

    "p4301": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4302": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4303": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4304": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },

    "p4305": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4306": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4307": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4308": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },

    "p4309": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4310": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4311": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4312": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },

    "p4313": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4314": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4315": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
    "p4316": {
        '-1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 2,
                'recognition_count': 4,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 90,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 6,
                'recognition_count': 10,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '-4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 60,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 4,
                'recognition_count': 8,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '10': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '20': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': 130,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': 0,
                'recognition_count': 0,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },

        '2': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '3': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '4': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '1': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_DESKTOP,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

        '6': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '7': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 4000,
                'gradual_exit': 100,
            }
        },
        '8': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 340,
                'slide_up': 10,
                'gradual_entry': 100,
                'gradual_exit': 100,
            }
        },
        '5': {
            'task': {
                'type': TASK_TYPE_PROOFREADING,
                'duration': EXPECTED_READING_TASK_DURATION_SECONDS,
                'location': TASK_LOCATION_GLASS,
                'mobility': MOBILITY_SITTING,
            },
            'notification': {
                'type': '5_word',
                'count': TASK_PROOFREADING_NOTIFICATION_COUNT,
                'recognition_count': TASK_PROOFREADING_RECOGNITION_COUNT,
                'duration': NOTIFICATION_DURATION_MILLIS,
                'display_type': 'PROGRESSIVE_WITH_NO_REFRESH',
                'slide_down': 10,
                'slide_up': 10,
                'gradual_entry': 2000,
                'gradual_exit': 100,
            }
        },

    },
}

# print(get_all_sessions('p411'))
