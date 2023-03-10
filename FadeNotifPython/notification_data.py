# coding=utf-8

import utilities
from random import shuffle

NOTIFICATION_TYPE_5_WORD = '5_word'

SEQUENCE_FILE_TEST_NOTIFICATION = '_sequence_test_notifications.json'
MAX_AGE_OF_SAVED_DATA_MINUTES = 60


def get_all_notifications(notification_type):
    if notification_type == NOTIFICATION_TYPE_5_WORD:
        return NOTIFICATION_LIST_5_WORD.copy()
    else:
        print(f'Unsupported type: {notification_type}')
        return []


def get_next_notifications(notification_type, notification_count, participant=None):
    return [get_next_notification(notification_type, participant) for _ in
            range(notification_count)]


def get_next_notification(notification_type, participant):
    if notification_type == NOTIFICATION_TYPE_5_WORD:
        return _get_next_notification(NOTIFICATION_TYPE_5_WORD, NOTIFICATION_LIST_5_WORD,
                                      participant)
    else:
        print(f'Unsupported type: {notification_type}')
        return {}


def _get_next_notification(notification_type, notification_list, participant):
    # check stored values
    index, order = _get_sequence_object_info(participant, notification_type)
    # create new if there is none
    if order is None:
        print(f'    Creating new notification order: {notification_type}')
        index = -1
        order = list(range(len(notification_list)))
        shuffle(order)
    else:
        print('     Loading the previous notification order')

    index += 1
    if index > len(notification_list):
        index = 0

    # save current values
    _save_sequence_object_info(participant, notification_type, index, order)

    actual_index = order[index]
    return notification_list[actual_index].copy()


### -------  keeping index and order of used notifications (to avoid repeating after restarting the app)

sequence_notification_info_object = {}


def _get_sequence_history_file(participant):
    if participant is None:
        return SEQUENCE_FILE_TEST_NOTIFICATION
    else:
        return f'data/{participant}/_{participant}{SEQUENCE_FILE_TEST_NOTIFICATION}'


def _get_sequence_object_info(participant, notification_type):
    global sequence_notification_info_object

    sequence_file = _get_sequence_history_file(participant)

    index = sequence_notification_info_object.get(f'{notification_type}_index')
    order = sequence_notification_info_object.get(f'{notification_type}_order')

    # check whether there is saved data {"<type>_index": <index>, "<type>_order": <list>}
    if index is None and order is None:
        saved_data = utilities.read_json_data(sequence_file, MAX_AGE_OF_SAVED_DATA_MINUTES)
        index = saved_data.get(f'{notification_type}_index')
        order = saved_data.get(f'{notification_type}_order')

    return index, order


def _save_sequence_object_info(participant, notification_type, index, order):
    global sequence_notification_info_object

    sequence_file = _get_sequence_history_file(participant)

    sequence_notification_info_object[f'{notification_type}_index'] = index
    sequence_notification_info_object[f'{notification_type}_order'] = order

    utilities.save_json_data(sequence_file, sequence_notification_info_object)


### -------  notifications


# notification = {
#     "id": 1,
#     "iconColor": "#ffffffff",
#     "iconName": "battery50",
#     "appName": "Battery",
#     "title": "Power is low",
#     "message": "Please recharge before 5% left",
# }

NOTIFICATION_LIST_5_WORD = [
    {
        "id": 1,
        "title": "Most people sleep at night.",
        "alternative": "They woke up in the morning."
    },
    {
        "id": 2,
        "title": "He always buys fresh fruits.",
        "alternative": "She always sells fresh vegetables."
    },
    {
        "id": 3,
        "title": "There are friends among us.",
        "alternative": "The army had many foes."
    },
    {
        "id": 4,
        "title": "Our train's on platform three.",
        "alternative": "We booked the morning bus."
    },
    {
        "id": 5,
        "title": "My two friends are soldiers.",
        "alternative": "They had four good drivers."
    },
    {
        "id": 6,
        "title": "This place has nice carpets.",
        "alternative": "The house was decorated nicely."
    },
    {
        "id": 7,
        "title": "They believed what you said.",
        "alternative": "Do not trust drunk people."
    },
    {
        "id": 8,
        "title": "There are three rooms upstairs.",
        "alternative": "Ground floor has a pool."
    },
    {
        "id": 9,
        "title": "That computer does not work.",
        "alternative": "His phone is brand new."
    },
    {
        "id": 10,
        "title": "People love to give advice.",
        "alternative": "They do not follow guidelines."
    },
    {
        "id": 11,
        "title": "We were studying very hard.",
        "alternative": "They were playing on ground."
    },
    {
        "id": 12,
        "title": "The summer weather is good.",
        "alternative": "Autumn festival is well celebrated."
    },
    {
        "id": 13,
        "title": "My nephew has three phones.",
        "alternative": "I have four smartphones."
    },
    {
        "id": 14,
        "title": "It will probably rain soon.",
        "alternative": "The sun will rise soon."
    },
    {
        "id": 15,
        "title": "Some people like spicy food.",
        "alternative": "Little kids like sweet bread."
    },
    {
        "id": 16,
        "title": "Those two words are similar.",
        "alternative": "They are two complex sentences."
    },
    {
        "id": 17,
        "title": "Remember to bring your coat.",
        "alternative": "Don't forget to dress properly."
    },
    {
        "id": 18,
        "title": "My mother made me breakfast.",
        "alternative": "Your father prepared the meals."
    },
    {
        "id": 19,
        "title": "We became very good friends.",
        "alternative": "They became very strong foes."
    },
    {
        "id": 20,
        "title": "Thanks for the lovely party.",
        "alternative": "We have a wonderful event."
    },
    {
        "id": 21,
        "title": "I must find baggage reclaim.",
        "alternative": "Pack your items before boarding."
    },
    {
        "id": 22,
        "title": "These people waited in line.",
        "alternative": "The queue was very long."
    },
    {
        "id": 23,
        "title": "We raised our child together.",
        "alternative": "He guided the startup company."
    },
    {
        "id": 24,
        "title": "This morning I went shopping.",
        "alternative": "We bought items from store."
    },
    {
        "id": 25,
        "title": "Jane entered the room quietly.",
        "alternative": "He did not attend class."
    },
    {
        "id": 26,
        "title": "Please write a full paragraph.",
        "alternative": "Please read the whole passage."
    },
    {
        "id": 27,
        "title": "The swiss chocolate are cheap.",
        "alternative": "I like swiss chocolate more."
    },
    {
        "id": 28,
        "title": "She was pleased about this.",
        "alternative": "He praised the good work."
    },
    {
        "id": 29,
        "title": "She printed out three copies.",
        "alternative": "Do not waste printing paper."
    },
    {
        "id": 30,
        "title": "That line is perfectly straight.",
        "alternative": "Your circle is too small."
    },
    {
        "id": 31,
        "title": "Some materials are very warm.",
        "alternative": "Stay away from cold drinks."
    },
    {
        "id": 32,
        "title": "He has very sensitive skin.",
        "alternative": "She always applies sun cream."
    },
    # {
    #     "id": 33,
    #     "title": "Autumn is windy and cloudy.",
    #     "alternative": "Summer is warm and bright."
    # },
    {
        "id": 34,
        "title": "I understand the lesson now.",
        "alternative": "Your example was very clear."
    },
    {
        "id": 35,
        "title": "The workers are very healthy.",
        "alternative": "They got headaches after drinking."
    },
    {
        "id": 36,
        "title": "I have never been unemployed.",
        "alternative": "She got a permanent job."
    },
    {
        "id": 37,
        "title": "That dress was very expensive.",
        "alternative": "The gown makes her beautiful."
    },
    {
        "id": 38,
        "title": "I started school in September.",
        "alternative": "We got vacations in December."
    },
    {
        "id": 39,
        "title": "My landlady cooks awful meals.",
        "alternative": "Her mother cooks tasty food."
    },
    {
        "id": 40,
        "title": "Most people like travel abroad.",
        "alternative": "They loved to visit countryside."
    },
    {
        "id": 41,
        "title": "They entered the room together.",
        "alternative": "They always stuck with each."
    },
    {
        "id": 42,
        "title": "I think insects are disgusting.",
        "alternative": "Worms can cause stomach pain."
    },
    {
        "id": 43,
        "title": "He finished reading the letters.",
        "alternative": "She wrote almost all letters."
    },
    {
        "id": 44,
        "title": "My favourite colour is orange.",
        "alternative": "Green is pleasing my eyes."
    },
    {
        "id": 45,
        "title": "We lifted many boxes today.",
        "alternative": "They helped to carry luggage."
    },
    {
        "id": 46,
        "title": "My mother lives in town.",
        "alternative": "Father visited village today."
    },
    {
        "id": 47,
        "title": "I repeated myself three times.",
        "alternative": "We check the marking twice."
    },
    {
        "id": 48,
        "title": "It has happened several times.",
        "alternative": "He forgot to bring lunch."
    },
    {
        "id": 49,
        "title": "That woman has beautiful hair.",
        "alternative": "My cousin is very handsome."
    },
    {
        "id": 50,
        "title": "Look at that chemical solution.",
        "alternative": "Organic food is very expensive."
    },
    {
        "id": 51,
        "title": "Farmers are very special people.",
        "alternative": "They farmed the whole land."
    },
    {
        "id": 52,
        "title": "My holiday is seventeen days.",
        "alternative": "I have eight extra leaves."
    },
    {
        "id": 53,
        "title": "Weather condition is getting bad.",
        "alternative": "Flood started to get worse."
    },
    {
        "id": 54,
        "title": "There are many different symbols.",
        "alternative": "See the similarity between each."
    },
    {
        "id": 55,
        "title": "Science class is very interesting.",
        "alternative": "I find maths very fascinating."
    },
    {
        "id": 56,
        "title": "I gave presents to everybody.",
        "alternative": "He always chose valuable gifts."
    },
    {
        "id": 57,
        "title": "Everybody wants to gain success.",
        "alternative": "Failures do not block progress."
    },
    {
        "id": 58,
        "title": "Calculator is a difficult word.",
        "alternative": "Sun and son are confusing."
    },
    {
        "id": 59,
        "title": "I like everything except onions.",
        "alternative": "My favorite dish is potatoes."
    },
    {
        "id": 60,
        "title": "They cried at the funeral.",
        "alternative": "His death made them sad."
    },
    {
        "id": 61,
        "title": "The colour is very bright.",
        "alternative": "Use warm light for interior."
    },
    {
        "id": 62,
        "title": "We drove through a tunnel.",
        "alternative": "The bridge was very long."
    },
    {
        "id": 63,
        "title": "I found ten dollars today.",
        "alternative": "He earns his daily salary."
    },
    {
        "id": 64,
        "title": "The house is burning down.",
        "alternative": "Firefighters arrived at the scene."
    },
    {
        "id": 65,
        "title": "I have an orange envelope.",
        "alternative": "She put stamps on envelopes."
    },
    {
        "id": 66,
        "title": "They are very nice people.",
        "alternative": "It was nice talking to you."
    },
    {
        "id": 67,
        "title": "Please use the main doors.",
        "alternative": "The main entrance was blocked."
    },
    {
        "id": 68,
        "title": "This place is always open.",
        "alternative": "It closed only for renovation."
    },
    {
        "id": 69,
        "title": "He always tells the truth.",
        "alternative": "Tell the truth to teacher."
    },
    {
        "id": 70,
        "title": "I will clean the bathroom.",
        "alternative": "The store was very clean."
    },
    {
        "id": 71,
        "title": "I need this new software.",
        "alternative": "That software was very bulky."
    },
    {
        "id": 72,
        "title": "I already knew about that.",
        "alternative": "We knew they had issues."
    },
    {
        "id": 73,
        "title": "To learn English is easy.",
        "alternative": "Learning Spanish is very hard."
    },
    # {
    #     "id": 74,
    #     "title": "Winter in Ontario is cold.",
    #     "alternative": "Orleans has long cold winters."
    # },
    {
        "id": 75,
        "title": "Give me the phone, please.",
        "alternative": "Please limit your phone usage."
    },
    {
        "id": 76,
        "title": "Four hours have passed by.",
        "alternative": "We waited six hours continuously."
    },
    {
        "id": 77,
        "title": "This is a marvelous meal.",
        "alternative": "Their food is really great."
    },
    {
        "id": 78,
        "title": "That is a simple question.",
        "alternative": "That question was very hard."
    },
    {
        "id": 79,
        "title": "He is wearing his pyjamas.",
        "alternative": "Don't go outside in pyjamas."
    },
    {
        "id": 80,
        "title": "I love your cheese spread.",
        "alternative": "I have a cheese sandwich."
    },
    {
        "id": 81,
        "title": "I had three cookies today.",
        "alternative": "I don't eat between meals."
    },
    {
        "id": 82,
        "title": "You got here very quickly.",
        "alternative": "He arrived late for work."
    },
    {
        "id": 83,
        "title": "They will help each other.",
        "alternative": "I will probably help him."
    },
    {
        "id": 84,
        "title": "She can make a difference.",
        "alternative": "She said she will return."
    },
    {
        "id": 85,
        "title": "I need an electric stove.",
        "alternative": "She bought an electric kettle."
    },
    {
        "id": 86,
        "title": "He teaches me at weekends.",
        "alternative": "Her teaching style is excellent."
    },
    {
        "id": 87,
        "title": "I like reading very much.",
        "alternative": "Don't listen to his readings."
    },
    {
        "id": 88,
        "title": "You made the right guess.",
        "alternative": "Think before you guess answer."
    },
    {
        "id": 89,
        "title": "The car belongs to them.",
        "alternative": "I bought my car yesterday."
    },
    {
        "id": 90,
        "title": "She is very kind hearted.",
        "alternative": "His kindness saved us all."
    },
    {
        "id": 91,
        "title": "That was an exciting game.",
        "alternative": "It was a deliberate foul."
    },
    {
        "id": 92,
        "title": "This is a valuable metal.",
        "alternative": "It was bright and shiny."
    },
    {
        "id": 93,
        "title": "We need oxygen to breathe.",
        "alternative": "Oxygen help plants to grow."
    },
    {
        "id": 94,
        "title": "You picked the right one.",
        "alternative": "Pick fresh vegetables for lunch."
    },
    {
        "id": 95,
        "title": "I work for the government.",
        "alternative": "Government job is more secure."
    },
    {
        "id": 96,
        "title": "You aren't wearing a tie.",
        "alternative": "Your tie doesn't fit well."
    },
    {
        "id": 97,
        "title": "All these chairs are free.",
        "alternative": "Some chairs have minor damages."
    },
    {
        "id": 98,
        "title": "I love my chocolate milk.",
        "alternative": "Butter is made from milk."
    },
    {
        "id": 99,
        "title": "He carried it by himself.",
        "alternative": "Do not carry heavy weight."
    },
    {
        "id": 100,
        "title": "That bird is flying high.",
        "alternative": "We failed to catch birds."
    },
    {
        "id": 101,
        "title": "The taxi is arriving now.",
        "alternative": "The taxi has been booked."
    },
    {
        "id": 102,
        "title": "The journey home is long.",
        "alternative": "How long until we're home?"
    },
    {
        "id": 103,
        "title": "Please don't point at me.",
        "alternative": "I do not like attention."
    },
    {
        "id": 104,
        "title": "I have a small appetite.",
        "alternative": "I have a slow metabolism."
    },
    {
        "id": 105,
        "title": "They are in the library.",
        "alternative": "I'll study in the library."
    },
    {
        "id": 106,
        "title": "We haven't got much time.",
        "alternative": "Can you please hurry up?"
    },
    {
        "id": 107,
        "title": "That bear is really big.",
        "alternative": "Panda bears are so cute."
    },
    {
        "id": 108,
        "title": "Your music is very loud.",
        "alternative": "Can you wear headphones please?"
    },
    {
        "id": 109,
        "title": "Give me all the details.",
        "alternative": "Tell me everything you heard."
    },
    {
        "id": 110,
        "title": "Their house is very big.",
        "alternative": "They have a large house."
    },
    {
        "id": 111,
        "title": "Love is a strong emotion.",
        "alternative": "Hate is a strong emotion."
    },
    {
        "id": 112,
        "title": "That is a compound word.",
        "alternative": "What is a good adjective?"
    },
    {
        "id": 113,
        "title": "I brought him a present.",
        "alternative": "How many days until Christmas?"
    },
    {
        "id": 114,
        "title": "My mother's a good cook.",
        "alternative": "My father likes baking bread."
    },
    {
        "id": 115,
        "title": "They must have a doctor.",
        "alternative": "I will call an ambulance."
    },
    {
        "id": 116,
        "title": "It was bright and shiny.",
        "alternative": "Look at my diamond ring."
    },
    {
        "id": 117,
        "title": "This is a good magazine.",
        "alternative": "This article is so interesting."
    },
    {
        "id": 118,
        "title": "I like bread and butter.",
        "alternative": "I will churn some butter."
    },
    {
        "id": 119,
        "title": "Can you make apple pies?",
        "alternative": "They made a pumpkin pie."
    },
    {
        "id": 120,
        "title": "Will they leave with you?",
        "alternative": "They don't want to leave."
    },
    {
        "id": 121,
        "title": "Meet at the bus interchange.",
        "alternative": "Hurry, the bus is departing."
    },
    {
        "id": 122,
        "title": "He organized a poetry show.",
        "alternative": "I just bought event tickets."
    },
    {
        "id": 123,
        "title": "She started a new job.",
        "alternative": "I will be starting soon."
    },
    {
        "id": 124,
        "title": "I got a speeding ticket.",
        "alternative": "You drive away too quickly."
    },
    {
        "id": 125,
        "title": "Graphic design is my passion.",
        "alternative": "Please don't use comic sans."
    },
    {
        "id": 126,
        "title": "Genna has an exam today.",
        "alternative": "I have an assignment due."
    },
    {
        "id": 127,
        "title": "He has good music taste.",
        "alternative": "I just bought new speakers."
    },
    {
        "id": 128,
        "title": "Do you like his seminar?",
        "alternative": "The class is very boring."
    },
    {
        "id": 129,
        "title": "She is now a veterinarian.",
        "alternative": "Help, my hamster is unwell."
    },
    {
        "id": 130,
        "title": "Can you start cooking dinner?",
        "alternative": "Anya will bring pasta later."
    },
    {
        "id": 131,
        "title": "I will be retiring soon.",
        "alternative": "She is leaving her job."
    },
    {
        "id": 132,
        "title": "Please turn off the oven.",
        "alternative": "Turn the lights off please."
    },
    {
        "id": 133,
        "title": "What is for dinner tonight?",
        "alternative": "I had sandwiches for lunch."
    },
    {
        "id": 134,
        "title": "The pineapple is very sweet.",
        "alternative": "Fruit tastes best when ripe."
    },
    {
        "id": 135,
        "title": "The weather is really good.",
        "alternative": "Let's hope it doesn't rain."
    }
]

### ------------

# count = 21
NOTIFICATION_LIST_ICONS_COLOR = [
    {
        "id": 1,
        "iconColor": "#ff00ff00",
        "iconName": "battery50",
        "appName": "Battery"
    },
    {
        "id": 2,
        "iconColor": "#ff4285f4",
        "iconName": "acc",
        "appName": "Contact"
    },
    {
        "id": 3,
        "iconColor": "#ff4285f4",
        "iconName": "chat",
        "appName": "Messenger"
    },
    {
        "id": 4,
        "iconColor": "#ff00ffff",
        "iconName": "backup",
        "appName": "Backup"
    },
    {
        "id": 5,
        "iconColor": "#ff888888",
        "iconName": "settings",
        "appName": "Settings"
    },
    {
        "id": 6,
        "iconColor": "#ff4285f4",
        "iconName": "alarm",
        "appName": "Alarm"
    },
    {
        "id": 7,
        "iconColor": "#ff4285f4",
        "iconName": "call",
        "appName": "Call"
    },
    {
        "id": 8,
        "iconColor": "#ff4285f4",
        "iconName": "news",
        "appName": "News"
    },
    {
        "id": 9,
        "iconColor": "#ff00ff00",
        "iconName": "whatsapp",
        "appName": "WhatsApp"
    },
    {
        "id": 10,
        "iconColor": "#ff00aff0",
        "iconName": "skype",
        "appName": "Skype"
    },
    {
        "id": 11,
        "iconColor": "#ff00ff00",
        "iconName": "hangout",
        "appName": "Hangout"
    },
    {
        "id": 12,
        "iconColor": "#ff888888",
        "iconName": "google_play",
        "appName": "Play"
    },
    {
        "id": 13,
        "iconColor": "#ffd44638",
        "iconName": "gmail",
        "appName": "Gmail"
    },
    {
        "id": 14,
        "iconColor": "#ff3b5998",
        "iconName": "facebook",
        "appName": "Facebook"
    },
    {
        "id": 15,
        "iconColor": "#ffffff00",
        "iconName": "snapchat",
        "appName": "SnapChat"
    },
    {
        "id": 16,
        "iconColor": "#ffff00ff",
        "iconName": "instagram",
        "appName": "Instagram"
    },
    {
        "id": 17,
        "iconColor": "#ffffff00",
        "iconName": "amazon",
        "appName": "Amazon"
    },
    {
        "id": 18,
        "iconColor": "#ffff0000",
        "iconName": "youtube",
        "appName": "YouTube"
    },
    {
        "id": 19,
        "iconColor": "#ff4285f4",
        "iconName": "google",
        "appName": "Google"
    },
    {
        "id": 20,
        "iconColor": "#ff00ffff",
        "iconName": "twitter",
        "appName": "Twitter"
    },
    {
        "id": 21,
        "iconColor": "#ff00ffff",
        "iconName": "calendar",
        "appName": "Calendar"
    },
]

# count = 20
NOTIFICATION_LIST_FULL_DATA = [
    {
        "id": 1,
        "iconColor": "#ffffffff",
        "iconName": "battery50",
        "appName": "Battery",
        "title": "Power is low",
        "message": "Please recharge before 5% left",
    },
    {
        "id": 2,
        "iconColor": "#ffffffff",
        "iconName": "acc",
        "appName": "Contact",
        "title": "Details have updated",
        "message": "Please refresh app to reload",
    },
    {
        "id": 3,
        "iconColor": "#ffffffff",
        "iconName": "chat",
        "appName": "Messenger",
        "title": "John sent a message",
        "message": "I am reaching the destination",
    },
    {
        "id": 4,
        "iconColor": "#ffffffff",
        "iconName": "backup",
        "appName": "Backup",
        "title": "File has changed",
        "message": "Please sync up with cloud",
    },
    {
        "id": 5,
        "iconColor": "#ffffffff",
        "iconName": "settings",
        "appName": "Settings",
        "title": "WiFi has deactivated",
        "message": "Trying to connect with internet",
    },
    {
        "id": 6,
        "iconColor": "#ffffffff",
        "iconName": "alarm",
        "appName": "Alarm",
        "title": "New timer added",
        "message": "Press play button to start",
    },
    {
        "id": 7,
        "iconColor": "#ffffffff",
        "iconName": "call",
        "appName": "Call",
        "title": "Missed voice call",
        "message": "Teacher attempted 10am today",
    },
    {
        "id": 8,
        "iconColor": "#ffffffff",
        "iconName": "news",
        "appName": "News",
        "title": "30\u2103 in Singapore",
        "message": "Scattered thunderstorms in the forecast",
    },
    {
        "id": 9,
        "iconColor": "#ffffffff",
        "iconName": "gmail",
        "appName": "Email",
        "title": "2 new messages",
        "message": "Swipe down to see content",
    },
    {
        "id": 10,
        "iconColor": "#ffffffff",
        "iconName": "cart",
        "appName": "Shopping",
        "title": "Discounts upto 50%",
        "message": "Amazing deals come your way",
    },
    {
        "id": 11,
        "iconColor": "#ffffffff",
        "iconName": "battery50",
        "appName": "Battery",
        "title": "Phone fully charged",
        "message": "Disconnect charger to save power",
    },
    {
        "id": 12,
        "iconColor": "#ffffffff",
        "iconName": "acc",
        "appName": "Contact",
        "title": "New number added",
        "message": "Successfully updated the additional info",
    },
    {
        "id": 13,
        "iconColor": "#ffffffff",
        "iconName": "chat",
        "appName": "Messenger",
        "title": "Exam results out",
        "message": "Your scores are available now",
    },
    {
        "id": 14,
        "iconColor": "#ffffffff",
        "iconName": "backup",
        "appName": "Backup",
        "title": "System is updating",
        "message": "Old files will be archived",
    },
    {
        "id": 15,
        "iconColor": "#ffffffff",
        "iconName": "settings",
        "appName": "Settings",
        "title": "Size has changed",
        "message": "Restart the app to load",
    },
    {
        "id": 16,
        "iconColor": "#ffffffff",
        "iconName": "alarm",
        "appName": "Alarm",
        "title": "Bedtime schedule active",
        "message": "See recent sleep history",
    },
    {
        "id": 17,
        "iconColor": "#ffffffff",
        "iconName": "call",
        "appName": "Call",
        "title": "Silent mode enabled",
        "message": "Please connect headphones to answer",
    },
    {
        "id": 18,
        "iconColor": "#ffffffff",
        "iconName": "news",
        "appName": "News",
        "title": "New COVID cluster",
        "message": "Schools closed until further notice",
    },
    {
        "id": 19,
        "iconColor": "#ffffffff",
        "iconName": "gmail",
        "appName": "Email",
        "title": "Dean's circular message",
        "message": "Resumption of campus operations Monday",
    },
    {
        "id": 20,
        "iconColor": "#ffffffff",
        "iconName": "cart",
        "appName": "Shopping",
        "title": "Waiting for payment",
        "message": "Select the card type bellow",
    },
]

# print(get_next_notifications(NOTIFICATION_TYPE_5_WORD, 3))
# print(get_next_notifications(NOTIFICATION_TYPE_5_WORD, 3))
