import logging
import asyncio

#-------------------
from database import init_db
from aiogram import Bot, Dispatcher
from handlers import router
from config import BOT_TOKEN

init_db()
async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token= str(BOT_TOKEN))
    dp = Dispatcher()
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


