from aiogram import Router, types
from aiogram.filters import CommandStart, Command
#-----------------------------------
router = Router()
#-----------------------------------

@router.message(CommandStart())
async def get_cmd_start(message: types.Message):
    await message.answer(f"Привет - {message.from_user.first_name}!\n Я бот на языке Python\n Если хотите узнать список команд пропишите \n\n /help")