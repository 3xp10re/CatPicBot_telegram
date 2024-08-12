import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from app.handlers import router
from app.parser import parse 

async def main():
    parse('https://www.pexels.com/ru-ru/search/кошка/')
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot is off')
