from aiogram import Router
from aiogram.types import Message
from .router import router
from ..keyboards.default.start import MAIN_INLINE_KEYBOARD
from flask_app.utils.db import get_user_data


@router.message()
async def bot_echo(message: Message):
    user_data = get_user_data(message.chat.username)
    if len(user_data):
        await message.answer(f'Привет, {user_data.get("name")} из города {user_data.get("city")}!',
                             reply_markup=None)
    else:
        await message.answer(f'Привет, {message.chat.username}. Я пока не знаю как тебя зовут и из какого ты города.'
                             f'Заполни форму и попробуй поздороваться снова.', reply_markup=MAIN_INLINE_KEYBOARD)
