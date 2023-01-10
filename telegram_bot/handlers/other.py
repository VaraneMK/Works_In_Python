from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


async def get_message(message=types.Message):
    await bot.send_message(chat_id=message.from_user.id,text='Я не понимаю Вашей просьбы((\nПожалуйста,воспользуйтесь клавиатурой', reply_markup=kb_client)



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(get_message)