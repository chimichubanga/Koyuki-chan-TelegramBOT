import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from cogs import main_menu, navigation, homework_list, webinar_records, bot_info, help

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=TOKEN)
# Инициализация диспетчера с использованием памяти для хранения состояний
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация обработчиков
main_menu.register_handlers(dp)
navigation.register_handlers(dp)
homework_list.register_handlers(dp)
webinar_records.register_handlers(dp)
bot_info.register_handlers(dp)
help.register_handlers(dp)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/menu", description="Показать меню")
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
