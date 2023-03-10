# coding=utf-8

## maps data to smart glass supported format

GLASS_NOTIFICATION_TYPE_HEADS_UP = 2


def get_empty_notification():
    return {
        "type": GLASS_NOTIFICATION_TYPE_HEADS_UP,
        "id": -1,
        "title": "",
    }


# notification_data: { "iconColor": <#color> , "iconName":  <app_icon> }
def _get_notification_icon(notification_data):
    if notification_data.get("iconName"):
        print(notification_data.get('iconName'))
        if notification_data.get("iconColor"):
            return f'{notification_data.get("iconColor")} {notification_data.get("iconName")}'
        else:
            return f'#FFFFFFFF {notification_data.get("iconName")}'
    else:
        return ""


def _get_notification_config(notification_data, config):
    if config: # non-empty config
        return config

    if notification_data.get("config"):
        return notification_data.get("config")

    return ''


def _get_notification_attribute(value):
    if value:
        return value
    else:
        return ''


# notification_data: { "id": <id>, "title": <title>, "message": <message> , "iconColor": <#color> , "iconName":  <app_icon>, "appName": <app_name> }
# all time related data in millis
def get_notification(notification_data, when, duration, config=None):
    return {
        "type": GLASS_NOTIFICATION_TYPE_HEADS_UP,
        "id": _get_notification_attribute(notification_data.get("id")),
        "title": _get_notification_attribute(notification_data.get("title")),
        "message": _get_notification_attribute(notification_data.get("message")),
        "appName": _get_notification_attribute(notification_data.get("appName")),
        "when": when,
        "duration": duration,
        "smallIcon": _get_notification_icon(notification_data),
        "config": _get_notification_config(notification_data, config)
    }


def get_updated_notification_with_reading_passage(notification, notification_config,
                                                  reading_question, when):
    # update when to show notification
    notification.update({"when": when})

    # append the question to the notification_config
    notification_config = "{},{},{},".format(notification_config,
                                             reading_question.get('Header', ''),
                                             reading_question.get('Passage').replace(",", "|"))
    notification.update({"config": notification_config})

    return notification


def get_updated_subsequent_notification(notification, notification_config, when):
    # update when to show notification
    notification.update({"when": when})

    # update config to support no refresh
    notification_config = "{},".format(
        notification_config.replace("PROGRESSIVE_WITH_DISPLAY", "PROGRESSIVE_WITH_NO_REFRESH"))
    notification.update({"config": notification_config})

    return notification


def get_mcq_display_data(question, options, selected=""):
    return {
        "heading": "{}".format(question),
        "content": "{}|{}|{}|{}|{}".format(
            options[0],
            options[1],
            options[2],
            options[3],
            selected),
        "config": "MCQ_CHOICES"
    }


def get_display_data_without_refresh(heading, subheading, content=""):
    return {
        "heading": heading,
        "subheading": subheading,
        "content": content,
        "config": "NO_REFRESH"
    }


def get_calibration_display_data():
    return {
        "subheading": "AA                                                          BB                                                          CC "
                      "\n\n\n"
                      "MM                                                         O                                                           PP "
                      "\n\n\n"
                      "XX                                                          YY                                                          ZZ"
    }


def get_center_point_display_data():
    return {
        "subheading": "\n\n\n                                                                LOL"
    }


def get_dummy_display_data():
    return {
        "subheading": "Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, "
                      "and printing in place of English to emphasise design elements over content. "
                      "It's also called placeholder (or filler) text. It's a convenient tool for mock-ups. "
                      "It helps to outline the visual elements of a document or presentation, "
                      "eg typography, font, or layout. Lorem ipsum is mostly a part of a Latin text "
                      "by the classical author and philosopher Cicero. Its words and letters have been "
                      "changed by addition or removal, so to deliberately render its content nonsensical;"
                      " it's not genuine, correct, or comprehensible Latin anymore."
    }


# reading_question = {
#     "Rating for complexity": 15.7,
#     "Id": 62,
#     "Word Count": 97,
#     "Sentence Count": 5,
#     "Flesch Reading Ease": 79.6,
#     "Reading Time": 23.26,
#     "Passage": "The analysis showed how much sugar is in hot drinks. An example is that a can of coke has an average of 10 teaspoons of sugar, but that's nothing compared to a Caramel Latte with 15 teaspoons of sugar. A Chai Latte has 20 teaspoons of sugar, and the worst offender is a Starbucks's hot mulled fruit drink with 25 teaspoons of sugar. That is three times more sugar than you should have in one day! Most sugar is in mochas and lattes. For now, it may be better for you to choose drinks with less sugar.",
#     "Question_1": "How many teaspoons does a can of coke contain?",
#     "Option1_1": 10,
#     "Option2_1": 15,
#     "Option3_1": 25,
#     "Option4_1": 20,
#     "Answer_1": 1,
#     "Question_2": "Which one has the highest sugar?",
#     "Option1_2": "Coke",
#     "Option2_2": "Latte",
#     "Option3_2": "Mocha",
#     "Option4_2": "Hot fruit drink",
#     "Answer_2": 4
# }

def get_mcq_reading_question_display_data(reading_question, question_number, selected=""):
    return get_mcq_display_data(
        reading_question["Question_{}".format(question_number)],
        [
            reading_question["Option1_{}".format(question_number)],
            reading_question["Option2_{}".format(question_number)],
            reading_question["Option3_{}".format(question_number)],
            reading_question["Option4_{}".format(question_number)],
        ],
        selected
    )


def get_notification_reading_question_display_data(notification_question, selected=""):
    return get_mcq_display_data(
        notification_question["Question"],
        [
            notification_question["Option1"],
            notification_question["Option2"],
            notification_question["Option3"],
            notification_question["Option4"]
        ],
        selected
    )
