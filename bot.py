from os import environ

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(environ["TG_TOKEN"])
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
