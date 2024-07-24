from aiogram import types, Dispatcher
from aiogram.filters import Command

async def send_welcome(message: types.Message):
    text = """
    **Добро пожаловать в Koyuki-chan!**

    Я Koyuki-chan, ваша виртуальная помощница, созданная для упрощения навигации по курсу "Код будущего".
    """
    
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📚 Список дз", callback_data="homework_list")],
        [types.InlineKeyboardButton(text="🎥 Записи вебинара", callback_data="webinar_records")],
        [types.InlineKeyboardButton(text="❓ Помощь", callback_data="help")],
        [types.InlineKeyboardButton(text="ℹ️ Информация о боте", callback_data="bot_info")]
    ])
    
    await message.answer(text, reply_markup=markup, parse_mode='Markdown')

def register_handlers(dp: Dispatcher):
    dp.message.register(send_welcome, Command("start"))
    dp.message.register(send_welcome, Command("menu"))
