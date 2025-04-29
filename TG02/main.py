import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import aiohttp
from config import TGTOKEN

from gtts import gTTS
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TGTOKEN)
dp = Dispatcher()


async def translate_to_english(text: str) -> str:
    """Translate text to English using Google Translate."""
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'https://translate.googleapis.com/translate_a/single',
            params={
                'client': 'gtx',
                'sl': 'auto',
                'tl': 'en',
                'dt': 't',
                'q': text,
            },
        ) as response:
            if response.status == 200:
                data = await response.json()
                return data[0][0][0]
            else:
                return "Ошибка перевода"


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')


@dp.message(Command('video'))
async def video(message: Message):
		await message.answer("Этот бот умеет выполнять команды:\\n/start\\n/help\\n/minitraining")

@dp.message(Command('video'))
async def video(message: Message):
		await message.answer("Этот бот умеет выполнять команды:\\n/start\\n/help\\n/minitraining")


@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   tts = gTTS(text=rand_tr, lang='ru')
   tts.save("tmp/training.ogg")
   audio = FSInputFile('tmp/training.ogg')
   await bot.send_voice(chat_id=message.chat.id, voice=audio)
   os.remove("tmp/training.ogg")
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")


@dp.message(F.photo)
async def react_photo(message: Message, bot: Bot):
    responses = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(responses)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(F.text)
async def translate_message(message: Message):
    translated_text = await translate_to_english(message.text)
    await message.answer(f"Перевод на английский: {translated_text}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
