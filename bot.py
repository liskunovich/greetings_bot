import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from tgbot import default_router

BOT_TOKEN = os.environ.get('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(default_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
