import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, FSInputFile, CallbackQuery

from gtts import gTTS
import os

from config import TGTOKEN
import keyboard as kb


bot = Bot(token=TGTOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Добро пожаловать!, {message.from_user.first_name}', reply_markup=kb.start_buttons)

@dp.message(F.text == "Привет")
async def hi_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.start_buttons)

@dp.message(F.text == "Пока")
async def bye_button(message: Message):
    await message.answer(f'Пока, {message.from_user.first_name}', reply_markup=kb.start_buttons)

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Полезные ссылки:', reply_markup=kb.links_buttons)

@dp.message(Command('dynamic'))
async def links(message: Message):
    await message.answer(f'Динамические кнопки:', reply_markup=kb.dynamic_buttons)


@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
   await callback.answer("Показываю больше")
   await callback.message.edit_text('Вот больше кнопок', reply_markup=kb.dynamic_buttons_more)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())