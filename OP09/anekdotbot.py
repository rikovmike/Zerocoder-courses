# t.me/rmJoker_bot.
# 7908138611:AAGzL8Ou0i8auP1TZzL6e5VUChvskAjT3Kw

import random

import requests
import telebot
from bs4 import BeautifulSoup


def get_random_joke():
    url = "https://anekdot.ru/"
    class_name = "topicbox"
    try:
        # Загружаем страницу
        response = requests.get(url)
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return ":( Не могу сейчас пошутить, шутки закончились"

    # Проверяем статус ответа
    if response.status_code != 200:
        print(f"Ошибка при загрузке страницы: {response.status_code}")
        return ":( Не могу сейчас пошутить, шутки закончились"

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все блоки div с заданным классом
    divs = soup.find_all('div', class_=class_name)

    content_array=[]
    for div in divs:
        nested_div = div.find('div', class_='text')  # Ищем вложенный div с классом "text"
        if nested_div:
            content_array.append(nested_div.get_text(strip=True))  # Извлекаем текст из вложенного div

    random_joke=random.choice(content_array)
    return random_joke


bot = telebot.TeleBot('7908138611:AAGzL8Ou0i8auP1TZzL6e5VUChvskAjT3Kw')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который попробует развеселить тебя случайным анекдотом!')

@bot.message_handler(commands=['joke'])
def start_message(message):
    bot.reply_to(message, get_random_joke())

bot.polling(none_stop=True)