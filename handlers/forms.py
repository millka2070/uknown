from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database import save_anket

router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    about = State()

def get_confirm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Да', callback_data='Yes_anket')],
            [InlineKeyboardButton(text='Нет', callback_data='No_anket')]
        ]
    )

@router.message(Command('form'))
async def start_form(message: types.Message, state: FSMContext):
    await message.answer('Введите ваше имя:')
    await state.set_state(Form.name)

@router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите возраст')
    await state.set_state(Form.age)

@router.message(Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой любимый цвет')
    await state.set_state(Form.about)

@router.message(Form.about)
async def process_about(message: types.Message, state: FSMContext):
    await state.update_data(about=message.text)
    data = await state.get_data()

    save_anket(message.from_user.id, data['name'], data['age'], data['about'])

    await message.answer(
        f"Вас зовут: {data['name']}\n"
        f"Вам: {data['age']}\n"
        f"Любимый цвет: {data['about']}\n"
        "Всё правильно?",
        reply_markup=get_confirm_keyboard()
    )
    await state.clear()

@router.callback_query(F.data == 'Yes_anket')
async def confirm_yes(callback: types.CallbackQuery):
    await callback.answer('Анкета сохранена!')

@router.callback_query(F.data == 'No_anket')
async def confirm_no(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите ваше имя:')
    await callback.answer()
    await state.set_state(Form.name)