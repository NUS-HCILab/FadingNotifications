# coding=utf-8

import display_formatter
import utilities

from pynput import keyboard
import threading
import time

DEVICE_IP_GLASS = '192.168.226.231'

MAX_RETRY_ATTEMPT = 3


def get_notification_url():
    return f'http://{DEVICE_IP_GLASS}:8080/notifiers/12/'


def get_display_url():
    return f'http://{DEVICE_IP_GLASS}:8080/displays/10/'


def get_touch_bar_url():
    return f'http://{DEVICE_IP_GLASS}:8080/touch/13'


def send_notification_data(notification):
    attempt = 0
    success = False
    while not success and attempt < MAX_RETRY_ATTEMPT:
        success = utilities.send_request(get_notification_url(), notification)
        attempt += 1

        if not success and attempt < MAX_RETRY_ATTEMPT:
            utilities.sleep_seconds(0.8)

    return success


def clear_notification_data():
    send_notification_data(display_formatter.get_empty_notification())


def is_not_blank(string):
    return bool(string and string.strip())


def send_reading_passage(passage=""):
    updated_passage = passage

    if is_not_blank(passage):
        # add extra lines to passage to avoid re-read the old content
        extra_lines = "\n\n\n\n\n\n\n\n\n\n\n\n"
        updated_passage = updated_passage + extra_lines

    display_data = display_formatter.get_display_data_without_refresh("", updated_passage, "")

    attempt = 0
    success = False
    while not success and attempt < MAX_RETRY_ATTEMPT:
        success = utilities.send_request(get_display_url(), display_data)
        attempt += 1

        if not success and attempt < MAX_RETRY_ATTEMPT:
            utilities.sleep_seconds(0.8)

    return success


def clear_reading_passage():
    send_reading_passage("")


# handle scrolling

def scroll(down):
    print(f'scroll:: down:{down}')
    if down:
        utilities.send_request(get_touch_bar_url(), {'type': 'ONE_FINGER_SWIPE_DOWN'})
    else:
        utilities.send_request(get_touch_bar_url(), {'type': 'ONE_FINGER_SWIPE_UP'})


def scroll_threaded(down):
    threading.Thread(target=scroll, args=(down,)).start()


def scroll_up():
    print('scroll_up')
    return utilities.send_request(get_touch_bar_url(), {'type': 'ONE_FINGER_SWIPE_UP'})


keyboard_listener = None


def enable_scrolling_listening():
    print('enable_scrolling_listening')
    global keyboard_listener
    keyboard_listener = keyboard.Listener(on_press=_on_press)
    keyboard_listener.start()


def disable_scrolling_listening():
    print('disable_scrolling_listening')
    global keyboard_listener
    keyboard_listener.stop()


last_key = None
last_key_press_time = 0


def _keep_key_info(key, key_time):
    global last_key, last_key_press_time
    last_key = key
    last_key_press_time = key_time


DEBOUNCE_SECONDS = 1  # 1 s


def _is_key_already_pressed(key, key_time):
    if key == last_key and key_time - last_key_press_time < DEBOUNCE_SECONDS:
        return True
    return False


def _on_press(key):
    current_time = time.time()

    # print("Key: ", key)
    if key == keyboard.Key.esc:
        return False  # stop listener

    # debounce the keys
    if _is_key_already_pressed(key, current_time):
        print('You have already pressed: ', key)
        return True

    if key == keyboard.Key.up:
        _keep_key_info(key, current_time)
        scroll(down=False)
        # scroll_threaded(down = False)

    if key == keyboard.Key.down:
        _keep_key_info(key, current_time)
        scroll(down=True)
        # scroll_threaded(down = True)
