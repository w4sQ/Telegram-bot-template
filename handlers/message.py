import logging

from aiogram import Dispatcher
from aiogram.types import Message
from Bot.keyboards import start_keyboard

logger = logging.getLogger(__name__)


async def start(message: Message):
    logger.debug("Function [start] get started.")
    await message.reply("Hello my friend!", reply_markup=start_keyboard())
    logger.debug("Function [start] finished.")


def register(dp: Dispatcher):
    """Registered message handlers"""
    dp.register_message_handler(start, commands="start")

    logger.debug("Message handlers register successful.")
