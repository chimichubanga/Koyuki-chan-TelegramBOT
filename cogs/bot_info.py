from aiogram import types, Dispatcher

async def handle_bot_info(call: types.CallbackQuery):
    text = """
    **О Koyuki-chan**

    Привет! Я Koyuki-chan, ваша виртуальная помощница, созданная для упрощения навигации по курсу Python. Моя миссия — помочь вам легко и удобно получать доступ к важной информации по курсу и домашним заданиям.

    **Мои возможности:**
    - 📚 **Список домашних заданий**: Я всегда готова дать вам список о текущих домашних заданиях и их дедлайнах.
    - 🎥 **Записи вебинаров**: Никогда не пропустите важный вебинар. Я предоставлю ссылки на все записи, чтобы вы могли пересматривать их в любое время.
    - ❓ **Помощь по курсу**: У вас есть вопросы по курсу? Я помогу найти нужную информацию и ответы.

    **О проекте:**
    - Моя разработка и поддержка осуществляются исключительно на чистом энтузиазме моего автора.

    **Исходный код:**
    - Вы можете найти исходный код проекта на [GitHub](https://github.com/chimichubanga/Koyuki-chan-TelegramBOT)

    **Контактная информация:**
    - **Автор**: [@chimichubanga](https://t.me/chimichubanga)
    - Если у вас есть предложения или замечания, пожалуйста, свяжитесь с моим автором. Мы всегда рады вашей обратной связи!

    Спасибо, что используете Koyuki-chan! Желаю вам успехов в изучении Python!
    """
    
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown')

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(handle_bot_info, lambda call: call.data == "bot_info")
