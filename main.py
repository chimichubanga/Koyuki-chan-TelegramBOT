# main.py
import telebot
from config import TOKEN
from cogs import main_menu, navigation, homework_list, webinar_records, bot_info

bot = telebot.TeleBot(TOKEN)

# Register cogs
main_menu.register_handlers(bot)
navigation.register_handlers(bot)
homework_list.register_handlers(bot)
webinar_records.register_handlers(bot)
bot_info.register_handlers(bot)

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
