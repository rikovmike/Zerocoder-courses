import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

import random
import requests

import nasa_api as nasaapi
import cat_api as catapi

from config import TOKEN, NASA_API_KEY
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def links(message: Message):
    await message.answer(f'Что ты хочешь увидеть сегодня?:', reply_markup=kb.main_buttons)

@dp.callback_query(F.data == 'nasa_rnd')
async def more(callback: CallbackQuery):
   apod = nasaapi.get_random_apod()
   photo_url = apod['url']
   title = apod['title']
   await callback.message.answer_photo(photo=photo_url, caption=f"{title}")
   await callback.message.answer(f'Что ты хочешь увидеть сегодня?:', reply_markup=kb.main_buttons)


@dp.callback_query(F.data == 'cat_rnd')
async def more(callback: CallbackQuery):
   breeds=catapi.get_cat_breeds()
   breed=random.choice(breeds)
   await callback.message.answer_photo(photo=breed['image']['url'],caption=breed['name'])
   await callback.message.answer(f'Что ты хочешь увидеть сегодня?:', reply_markup=kb.main_buttons)


async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())