"""Модуль запуска бота."""

import asyncio
import logging
import time

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_bot.handlers import router
from aiogram_bot.config_bot import config
from utils.logger_config import init_globals_logging

logger = logging.getLogger(__name__)
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(storage=MemoryStorage())
dispatcher.include_router(router)


async def main():
    """Функция запуска бота"""
    logger.info(f"Старт работы бота {int(time.time())}")
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    init_globals_logging()
    asyncio.run(main())
