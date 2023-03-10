# coding=utf-8


import utilities
import device_driver
import display_formatter

import notification_data
import reading_passages

NOTIFICATION_DURATION_MILLIS = 8000
CONSECUTIVE_REQUEST_GAP_SECONDS = 10

TRAINING_NOTIFICATIONS = [
    {
        "id": 1,
        "title": "Please recharge before 5% left",
        # "title": "That bear is really big.",
        # "config": "PROGRESSIVE_WITH_NO_REFRESH,10,10,100,100",
    },
    {
        "id": 2,
        "title": "Please sync up with cloud",
        # "title": "There are many different symbols.",
        # "config": "PROGRESSIVE_WITH_NO_REFRESH,340,340,100,100",
        # "config": "PROGRESSIVE_WITH_NO_REFRESH,10,10,100,100",
    },
    {
        "id": 3,
        "title": "Please refresh app to reload",
        # "title": "Weather condition is getting bad.",
        # "config": "PROGRESSIVE_WITH_NO_REFRESH,340,340,100,100",
        # "config": "PROGRESSIVE_WITH_NO_REFRESH,10,10,100,100",
    },
    {
        "id": 4,
        "title": "I am reaching the destination",
        # "title": "Science class is very interesting.",
        # "config": "PROGRESSIVE_WITH_NO_REFRESH,10,10,100,100",
    },
]

TRAINING_PASSAGES = [
    "Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in place of English to emphasise design elements over content. It's also called placeholder (or filler) text. "
    "It's a convenient tool for mock-ups. It helps to outline the visual elements of a document or presentation, eg typography, font, or layout. "
    "Lorem ipsum is mostly a part of a Latin text by the classical author and philosopher Cicero."
    " Its words and letters have been changed by addition or removal, so to deliberately render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. "
    "While lorem ipsum's still resembles classical Latin, it actually has no meaning whatsoever. "
    "As Cicero's text doesn't contain the letters K, W, or Z, alien to latin, these, and others are often inserted randomly to mimic the typographic appearance of European languages, as are digraphs not to be found in the original. "
    "In a professional context it often happens that private or corporate clients order a publication to be made and presented with the actual content still not being ready. "
    "Think of a news blog that's filled with content hourly on the day of going live. "
    "However, reviewers tend to be distracted by comprehensible content, say, a random text copied from a newspaper or the internet. "
    "The are likely to focus on the text, disregarding the layout and its elements. "
    "Besides, random text risks to be unintended humorous or offensive, an unacceptable risk in corporate environments. "
    "Lorem ipsum and its many variants have been employed since the early 1960ies, and quite likely since the sixteenth century."
    ,

]


def _get_config(type):
    if type == '0':
        return "PROGRESSIVE_WITH_NO_REFRESH,10,10,100,100"
    elif type == '2':
        return "PROGRESSIVE_WITH_NO_REFRESH,10,10,2000,100"
    elif type == '4':
        return "PROGRESSIVE_WITH_NO_REFRESH,10,10,4000,100"
    elif type == 't':
        return "PROGRESSIVE_WITH_NO_REFRESH,340,10,100,100"
    else:
        print(f'Type is undefined: [{type}]')

    return "PROGRESSIVE_WITH_NO_REFRESH,10,10,100,100"


notification_count = 0


def display_next_training_notification(type):
    global notification_count

    if notification_count >= len(TRAINING_NOTIFICATIONS):
        notification_count = 0

    notification = TRAINING_NOTIFICATIONS[notification_count].copy()
    notification["config"] = _get_config(type)

    device_driver.send_notification_data(display_formatter.get_notification(notification, 0, NOTIFICATION_DURATION_MILLIS))

    notification_count += 1

    utilities.sleep_seconds(CONSECUTIVE_REQUEST_GAP_SECONDS)


passage_count = 0


def display_next_training_passage():
    global passage_count

    if passage_count >= len(TRAINING_PASSAGES):
        passage_count = 0

    device_driver.send_reading_passage(TRAINING_PASSAGES[passage_count])

    passage_count += 1

    utilities.sleep_seconds(CONSECUTIVE_REQUEST_GAP_SECONDS/2)


def display_next_testing_notification():
    notification_content = notification_data.get_next_notification('5_word')
    device_driver.send_notification_data(
        display_formatter.get_notification(notification_content, 0, NOTIFICATION_DURATION_MILLIS,
                                           "PROGRESSIVE_WITH_NO_REFRESH,340,340,100,100"))
    utilities.sleep_seconds(CONSECUTIVE_REQUEST_GAP_SECONDS)


def display_next_testing_passage():
    device_driver.send_reading_passage(reading_passages.get_reading_passages(100)["text"])
    utilities.sleep_seconds(CONSECUTIVE_REQUEST_GAP_SECONDS/2)


# send scroll up event
device_driver.scroll(False)

_res = ''
while _res != 'n':
    _res = input("Continue? (p/0/2/4/t/n)")

    if _res == 't' or _res == '0' or _res == '2' or _res == '4':
        display_next_training_notification(_res)
    elif _res == 'p':
        display_next_training_passage()
    elif _res == 'rp':
        display_next_testing_passage()
    elif _res == 'rt':
        display_next_testing_notification()
    else:
        device_driver.clear_reading_passage()

device_driver.clear_reading_passage()
device_driver.clear_notification_data()
