import logging
import config_logging  # type: ignore

from aiogram import executor

from bot import dp
from handlers import message, callback


def main():
    logging.debug("test")
    message.register(dp)
    callback.register(dp)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
