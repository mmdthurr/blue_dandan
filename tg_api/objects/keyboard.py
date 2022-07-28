from enum import Enum, unique


@unique
class Switch(Enum):
    Current = 'switch_inline_query_current_chat'
    Other = 'switch_inline_query'


def keyboard_markup(
        keyboard,
        resize_keyboard=None,
        one_time_keyboard=None,
        input_field_placeholder=None,
        selective=None
):
    markup = {
        'keyboard': keyboard,
    }
    if resize_keyboard:
        markup['resize_keyboard'] = resize_keyboard
    if one_time_keyboard:
        markup['one_time_keyboard'] = one_time_keyboard
    if input_field_placeholder:
        markup['input_field_placeholder'] = input_field_placeholder
    if selective:
        markup['selective'] = selective
    return markup


def inline_markup(
        inline_keyboard: list
):
    markup = {
        'inline_keyboard': inline_keyboard
    }
    return markup


def keyboard_button(
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
):
    button = {
        'text': text,
    }
    if request_contact:
        button['request_contact'] = request_contact
    if request_location:
        button['request_location'] = request_location
    return button


def inline_button(
        text: str,
        url: str = None,
        callback_data: str = None
):
    button = {
        'text': text
    }
    if url:
        button['url'] = url
    if callback_data:
        button['callback_data'] = callback_data
    return button


def switch_inline(
        text: str,
        switch_str: str = '',
        switch: str = 'switch_inline_query_current_chat',
):
    button = {
        'text': text,
        switch: switch_str,
    }
    return button


def reply_keyboard_remove(
        selective: bool =None

):
    param = {
        'remove_keyboard': True
    }
    if selective:
        param['selective'] = selective
    return param
