import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import aiohttp
from config import TGTOKEN

API_TOKEN = TGTOKEN
WEATHER_API_KEY = '308f1ed66792108eb8f84b9405563d6f'  # Замените на ваш ключ OpenWeatherMap
GEOCODING_API_URL = 'http://api.openweathermap.org/geo/1.0/direct'
ONE_CALL_API_URL = 'https://api.openweathermap.org/data/3.0/onecall'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def fetch_weather(city: str) -> str:
    async with aiohttp.ClientSession() as session:
        # Step 1: Get coordinates of the city
        geocoding_params = {
            'q': city,
            'limit': 1,
            'appid': WEATHER_API_KEY
        }
        async with session.get(GEOCODING_API_URL, params=geocoding_params) as response:
            geocoding_data = await response.json()
            if response.status == 200 and geocoding_data:
                lat = geocoding_data[0]['lat']
                lon = geocoding_data[0]['lon']
                print(f"{city}: {lat} : {lon}")
            else:
                print(response)
                return "Не удалось найти город. Проверьте название города."

        # Step 2: Get weather data using the coordinates
        weather_params = {
            'lat': lat,
            'lon': lon,
            'exclude': 'minutely,hourly,daily,alerts',
            'units': 'metric',
            'lang': 'en',
            'appid': WEATHER_API_KEY
        }
        async with session.get(ONE_CALL_API_URL, params=weather_params) as response:
            weather_data = await response.json()
            if response.status == 200:
                weather_description = weather_data['current']['weather'][0]['description']
                temp = weather_data['current']['temp']
                return f"Погода в {city}: {weather_description}, температура {temp}°C"
            else:
                print(response)
                return "Не удалось получить данные о погоде."

@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.answer("Привет! Отправь мне название города, и я сообщу тебе прогноз погоды.")

@dp.message(lambda message: message.text.lower() == "отмена")
async def cancel_handler(message: Message):
    await message.answer("Запрос отменен.")

@dp.message()
async def get_weather(message: Message):
    city = message.text.strip()
    weather_info = await fetch_weather(city)
    await message.answer(weather_info)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())