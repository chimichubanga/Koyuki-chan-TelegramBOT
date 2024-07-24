from aiogram import types, Dispatcher
import logging
from aiogram.filters import CommandStart, Command

# Настройка логирования
logger = logging.getLogger(__name__)

async def log_user_action(message: types.Message):
    logger.info(f"User {message.from_user.id} used command {message.text}")

def register_handlers(dp: Dispatcher):
    dp.message.register(log_user_action, CommandStart())
    dp.message.register(log_user_action, Command(commands=['menu', 'help', 'homework_list', 'webinar_records', 'bot_info']))
