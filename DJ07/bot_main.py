import telebot
from telebot.types import Message
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000/api"

BOT_TOKEN = "7508072042:AAHE_HLKqhqjb-D76Q98fvXtV-XZEnBR9T8"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }
    print(data)
    response = requests.post(API_URL + "/register", json=data)

    if response.status_code == 200:  # Если успешный ответ
       bot.send_message(message.chat.id, "Вы уже были зарегистрированы ранее!")
    elif response.status_code == 201:  # Если успешный ответ
       bot.send_message(message.chat.id,
                             f"Вы успешно зарегистрированы! Ваш уникальный номер: {response.json()['id']}")
    else:  # Если ошибка
        bot.send_message(message.chat.id, "Произошла ошибка при регистрации!")
        #print(response.json())
        print(response.status_code)
        print(response.text)


@bot.message_handler(commands=['myinfo'])
def start_command(message):
    data = {
        "user_id": message.from_user.id,
    }
    print(data)
    response = requests.post(API_URL + "/myinfo", json=data)

    if response.status_code == 200:



       try:
           dt = datetime.strptime(response.json()['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
           regdate = dt.strftime("%d.%m.%Y в %H:%M:%S")
       except:
           regdate = response.json()['created_at']

       bot.send_message(message.chat.id, f"Ваши данные в системе:\n username: {response.json()['username']}\n зарегистрирован: {regdate}")

    else:  # Если ошибка
        bot.send_message(message.chat.id, "Вам нужно зарегистрироваться!")
        #print(response.json())
        print(response.status_code)
        print(response.text)










print("START")
bot.polling(none_stop=True)