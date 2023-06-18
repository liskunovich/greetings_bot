from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from ..keyboards.default.start import MAIN_KEYBOARD, MAIN_INLINE_KEYBOARD
from .router import router
from flask_app.utils.db import get_user_data


@router.message(Command('start'))
async def start(message: Message):
    user_data = get_user_data(message.chat.username)
    if len(user_data):
        await message.answer(f'Привет, {user_data.get("name")} из города {user_data.get("city")}!',
                             reply_markup=None)
    else:
        await message.answer(f'Привет, {message.chat.username}. Я пока не знаю как тебя зовут и из какого ты города.'
                             f'Заполни форму и попробуй поздороваться снова.', reply_markup=MAIN_INLINE_KEYBOARD)


@router.callback_query(Text('start'))
async def callback_start(callback: CallbackQuery):
    user_data = get_user_data(callback.message.chat.username)
    if len(user_data):
        await callback.message.edit_text(f'Привет, {user_data.get("name")} из города {user_data.get("city")}!')
        await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer()
