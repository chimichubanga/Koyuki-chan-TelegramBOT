from aiogram import types, Dispatcher

async def handle_homework_help(call: types.CallbackQuery):
    text = """
    **ПОМОЩЬ С ДЗ**

    Дополнительные материалы для первого ДЗ доступны по [ссылке](https://telegra.ph/Domashnee-zadanie-1---Znakomstvo-s-telegramm-botami-poluchenie-tokena-sozdanie-pervoj-komandy-07-24).

    Дополнительные материалы для второго ДЗ доступны по [ссылке](https://telegra.ph/Domashnee-zadanie-2---Sozdanie-telegramm-bota-s-obrabotkoj-sluchajnyh-chisel-i-dublirovaniem-soobshchenij-07-24).

    Дополнительные материалы для третьего ДЗ доступны по [ссылке](https://telegra.ph/Domashnee-zadanie-3---Sozdanie-Telegram-bota-dlya-sozdaniya-oprosov-07-24).

    Остальные материалы будут доступны чуть позже

    Так же доступен [GitHub](https://github.com/MishinIgor/KB_Py_Mod2/tree/master/Group-5) с которым мы работаем на вебинарах

    Если у вас возникли вопросы или проблемы с домашними заданиями, вот несколько советов:

    1. **Пересмотрите записи вебинаров**: Вебинары содержат много полезной информации, которая может помочь вам с выполнением домашних заданий.
    2. **Задайте вопрос в чате курса**: В чате всегда есть студенты и преподаватели, готовые помочь.
    3. **Свяжитесь с преподавателем**: Если вам нужна дополнительная помощь, не стесняйтесь обратиться к преподавателю.

    Контакты для поддержки:
    👩‍🏫 **Преподаватель:** Игорь Мишин [@Imishinigor](https://t.me/Imishinigor)
    👨‍💻 **Тьютор:** Александр Головачев [@YourBuduschee2](https://t.me/YourBuduschee2)
    🛟 **Кураторы:** Анастасия [@plastasya](https://t.me/plastasya) и Яна [@qtwec](https://t.me/qtwec)

    Вы также можете ознакомиться с теорией, необходимой для выполнения ДЗ, выбрав одно из заданий ниже.
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад в помощь", callback_data="help")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(handle_homework_help, lambda call: call.data == "homework_help")
