from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



start_buttons = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

links_buttons = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://news.mail.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/')],
   [InlineKeyboardButton(text="Видео", url='https://yandex.ru/video/')],
])

dynamic_buttons = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')],
])

dynamic_buttons_more = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Опция 1", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')],
   [InlineKeyboardButton(text="Опция 2", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')],
])
