from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from .constants import BUTTON_1, BUTTON_2, BUTTON_3, IN_FILD_PL

buttons = [
    [KeyboardButton(text=BUTTON_1)],
    [KeyboardButton(text=BUTTON_2)],
    [KeyboardButton(text=BUTTON_3)],
]

keyboard_main = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    input_field_placeholder=IN_FILD_PL,
)
