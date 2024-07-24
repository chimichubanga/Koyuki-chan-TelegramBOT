# cogs/main_menu.py
from telebot import types

def register_handlers(bot):
    @bot.message_handler(commands=['start', 'menu'])
    def send_welcome(message):
        text = """
        **Добро пожаловать в Koyuki-chan!**

        Я Koyuki-chan, ваша виртуальная помощница, созданная для упрощения навигации по курсу "Код будущего".
        """
        
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("📚 Список дз", callback_data="homework_list")
        btn2 = types.InlineKeyboardButton("🎥 Записи вебинара", callback_data="webinar_records")
        btn3 = types.InlineKeyboardButton("❓ Помощь", callback_data="help")
        btn4 = types.InlineKeyboardButton("ℹ️ Информация о боте", callback_data="bot_info")
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        
        bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')
