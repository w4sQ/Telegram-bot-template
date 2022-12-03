from aiogram import types


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    start_button = types.InlineKeyboardButton(text="Tap to start", callback_data="start")
    keyboard.add(start_button)
    return keyboard
