from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


async def commands_start(message:types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать!\nДанный бот умеет хранить написанные Вами рецепты и по требованию отправлять их обратно)', reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/TestMusicSpotifyBot')


async def functional(message:types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id, text='Нажав на кнопку "Загрузить" Вы сможете добавить новый рецепт, а кнопка "Удалить" выдаст Вам список ваших рецептов с функционалом удаления.')
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/TestMusicSpotifyBot')

async def message(message:types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id, text='Я не понимаю Вашей просьбы((\nПожалуйста,воспользуйтесь клавиатурой', reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/TestMusicSpotifyBot')

async def recipes(message:types.Message):
    await sqlite_db.get_info(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['Старт', 'Помощь'])
    dp.register_message_handler(functional, commands=['Возможности'])
    dp.register_message_handler(recipes, commands=['Рецепты'])
