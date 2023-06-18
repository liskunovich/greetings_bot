from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup

kb = [
    [KeyboardButton(text='/start')]
]
MAIN_KEYBOARD = ReplyKeyboardMarkup(keyboard=kb,
                                    input_field_placeholder='Нажмите, чтобы поздороваться.',
                                    resize_keyboard=True)

inline_kb = [
    [InlineKeyboardButton(
        text='Поздороваться',
        callback_data='start')],
]
MAIN_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=inline_kb)
