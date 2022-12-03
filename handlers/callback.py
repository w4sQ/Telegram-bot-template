import logging

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

logger = logging.getLogger(__name__)


async def test(call: CallbackQuery):
    logger.debug("Function [test] get started.")
    await call.message.delete()
    logger.debug("Function [test] finished.")


def register(dp: Dispatcher):
    """Registered callback handlers"""
    dp.register_callback_query_handler(test, text="start")

    logger.debug("Callback handlers register successful.")
