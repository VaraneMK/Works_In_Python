from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import bot, dp


class FSM_Admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    cooking = State()


# @dp.message_handler(commands=['Загрузить'],state=None)
async def cm_start(message: types.Message):
    await FSM_Admin.photo.set()
    await message.reply('Загрузите фото')


# Первый ответ
# @dp.message_handler(content_types=['photo'],state=FSM_Admin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_Admin.next()
    await message.reply('Введите название')


# Второй ответ
# @dp.message_handler(state=FSM_Admin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_Admin.next()
    await message.reply('Введите рецепт')


# Третий ответ
# @dp.message_handler(state=FSM_Admin.description)
async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSM_Admin.next()
    await message.reply('Напишите процесс приготовления')


async def load_cook(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cooking'] = message.text
    # Перенести в БД
    await message.reply('Готово!')
    await sqlite_db.sql_add_command(state)
    await state.finish()


# @dp.message_handler(state='*', commands='Отмена')
# @dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Хорошо')


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'Рецепт для {callback_query.data.replace("del ", "")} удален.', show_alert=True)


# @dp.register_message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    read = await sqlite_db.get_info_2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0],
                             f'Название: {ret[1]}\nРецепт:\n{ret[2]}\nПроцесс приготовления:\n{ret[3]}')
        await bot.send_message(message.from_user.id, text='<----->', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Загрузить', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSM_Admin.photo)
    dp.register_message_handler(load_name, state=FSM_Admin.name)
    dp.register_message_handler(load_desc, state=FSM_Admin.description)
    dp.register_message_handler(load_cook, state=FSM_Admin.cooking)
    dp.register_message_handler(cancel_handler, state='*', commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(delete_item, commands='Удалить')

