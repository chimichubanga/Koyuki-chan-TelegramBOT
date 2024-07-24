# cogs/help.py
from telebot import types

def register_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "help")
    def handle_help(call):
        text = """
        **ПОМОЩЬ**

        Добро пожаловать в раздел помощи Koyuki-chan! Выберите один из разделов ниже:
        """
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("📝 Помощь с дз", callback_data="homework_help")
        btn2 = types.InlineKeyboardButton("❓ Частые вопросы", callback_data="faq")
        btn_back = types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="back_to_menu")
        markup.add(btn1, btn2)
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    @bot.callback_query_handler(func=lambda call: call.data == "homework_help")
    def handle_homework_help(call):
        text = """
        **ПОМОЩЬ С ДЗ**

        Если у вас возникли вопросы или проблемы с домашними заданиями, вот несколько советов:
        
        1. Пересмотрите записи вебинаров, связанные с темой задания.
        2. Обратитесь к материалам курса и учебникам.
        3. Задайте вопрос в чате курса или свяжитесь с преподавателем.

        Контакты для поддержки:
        - **Милан** [@chimichubanga](https://t.me/chimichubanga)

        Мы всегда рады помочь вам!
        """
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в помощь", callback_data="help")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    @bot.callback_query_handler(func=lambda call: call.data == "faq")
    def handle_faq(call):
        text = """
        **ЧАСТЫЕ ВОПРОСЫ (FAQ)**

        Выберите один из разделов ниже:
        """
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("📖 Ликбез", callback_data="basics")
        btn2 = types.InlineKeyboardButton("📚 Инструкция по LMS", callback_data="lms_guide")
        btn3 = types.InlineKeyboardButton("✉️ Написать куратору", callback_data="contact_curator")
        btn_back = types.InlineKeyboardButton("⬅️ Назад в помощь", callback_data="help")
        markup.add(btn1, btn2)
        markup.add(btn3)
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    @bot.callback_query_handler(func=lambda call: call.data == "basics")
    def handle_basics(call):
        text = """
        **ЛИКБЕЗ**

        👩‍🏫 **Преподаватель/Лектор** - к ним можно обращаться, если возникают вопросы о материале, пройденном на вебинаре.

        👨‍💻 **Тьюторы** - опытные программисты, которые помогут с освоением учебного материала. Они проверят домашние работы и подскажут, если возникнут сложности с заданиями.

        🛟 **Кураторы** (Анастасии @plastasya и Яна @qtwec) - спасательный круг, справочный центр, ваша фея-крестная с тапочкой вместо волшебной палочки (тапочка ускоряет сдачу ДЗ вне зависимости от обстоятельств). 
        Ей можно задать любой вопрос, ответ на который не найден в канале. Она поможет всем и всегда, особенно если написать заранее. 
        Единственный минус - куратор не программист, так что если вопрос о способе выполнения домашней работы - вас отправят к тьютору. Если тьютор долго не отвечает - пишем об этом куратору.

        📚 **ЛМС** - система, в которой вы будете выполнять домашние задания.

        💻 **МТС Линк** - платформа для просмотра вебинаров.
        Кто будет смотреть вебинар с ПК, ноутбука - просто открывайте ссылку на вебинар.
        Если вы смотрите вебинар с телефона - качайте приложение. 
        Пожалуйста, не перепутайте!

        📅 **Срок сдачи ДЗ** - даты, к которым нужно выполнить домашние задания и тест, если не хотите получать миллион звонков от других кураторов/менеджеров (родителям тоже будем звонить, да).
        Если у вас есть какие-то трудности с домашними заданиями, не хватает времени, нет желания вообще, то скажите своему куратору об этом сразу, а не игнорируйте.
        """
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в частые вопросы", callback_data="faq")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    @bot.callback_query_handler(func=lambda call: call.data == "lms_guide")
    def handle_lms_guide(call):
        text = """
        **ИНСТРУКЦИЯ ПО LMS**

        В этом разделе вы найдете руководство по использованию LMS.

        Полная инструкция доступна по ссылке: [ссылка](https://telegra.ph/INSTRUKCIYA-PO-POLZOVANIYU-LMS-07-24)
        """
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в частые вопросы", callback_data="faq")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    @bot.callback_query_handler(func=lambda call: call.data == "contact_curator")
    def handle_contact_curator(call):
        text = """
        **НАПИСАТЬ КУРАТОРУ**

        Если у вас есть вопросы или предложения, свяжитесь с одним из наших кураторов:

        👩‍🏫 **Преподаватель:** Игорь Мишин [@Imishinigor](https://t.me/Imishinigor)
        👨‍💻 **Тьютор:** Александр Головачев [@YourBuduschee2](https://t.me/YourBuduschee2)
        🛟 **Кураторы:** Анастасия [@plastasya](https://t.me/plastasya) и Яна [@qtwec](https://t.me/qtwec)
        """
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в частые вопросы", callback_data="faq")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
