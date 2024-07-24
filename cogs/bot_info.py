# cogs/bot_info.py
from telebot import types

def register_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "bot_info")
    def handle_bot_info(call):
        text = """
        **О Koyuki-chan**

        Привет! Я Koyuki-chan, ваша виртуальная помощница, созданная для упрощения навигации по курсу Python. Моя миссия — помочь вам легко и удобно получать доступ к важной информации по курсу и домашним заданиям.

        **Мои возможности:**
        - 📚 **Список домашних заданий**: Я всегда готова дать вам список о текущих домашних заданиях и их дедлайнах.
        - 🎥 **Записи вебинаров**: Никогда не пропустите важный вебинар. Я предоставлю ссылки на все записи, чтобы вы могли пересматривать их в любое время.
        - ❓ **Помощь по курсу**: У вас есть вопросы по курсу? Я помогу найти нужную информацию и ответы.

        **О проекте:**
        - Моя разработка и поддержка осуществляются исключительно на чистом энтузиазме моего автора.

        **Контактная информация:**
        - **Автор**: [@chimichubanga](https://t.me/chimichubanga)
        - Если у вас есть предложения или замечания, пожалуйста, свяжитесь с моим автором. Мы всегда рады вашей обратной связи!

        Спасибо, что используете Koyuki-chan! Желаю вам успехов в изучении Python!
        """
        
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("Назад в меню", callback_data="back_to_menu")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown')
