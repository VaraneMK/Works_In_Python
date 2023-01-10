from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/Возможности')
b2 = KeyboardButton('/Помощь')
b3 = KeyboardButton('/Рецепты')
b4 = KeyboardButton('/Загрузить')
b5 = KeyboardButton('/Удалить')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b2).add(b1).insert(b3).row(b4, b5)
