from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

memory_storage = MemoryStorage()


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory_storage)
