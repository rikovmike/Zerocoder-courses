from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main_buttons = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Рандомная фотка из NASA", callback_data='nasa_rnd')],
   [InlineKeyboardButton(text="Рандомная фотка кота", callback_data='cat_rnd')],
])

