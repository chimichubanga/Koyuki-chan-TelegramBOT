from aiogram import types, Dispatcher

async def handle_homework_help(call: types.CallbackQuery):
    text = """
    **ПОМОЩЬ С ДЗ**

    Вы можете ознакомиться с разбором и теорией, необходимой для выполнения ДЗ, выбрав одно из заданий ниже.
    
    Разбор домашнего задания для *1-го вебинара*. Тема: Знакомство с телеграмм ботами, получение токена, создание первой команды 
    ➡️ Разбор: [ссылка](https://telegra.ph/Domashnee-zadanie-1---Znakomstvo-s-telegramm-botami-poluchenie-tokena-sozdanie-pervoj-komandy-07-24).

    Разбор домашнего задания для *2-го вебинара*. Тема: Обработка команд пользователя, работа с текстовыми сообщениями 
    ➡️ Разбор: [ссылка](https://telegra.ph/Domashnee-zadanie-2---Sozdanie-telegramm-bota-s-obrabotkoj-sluchajnyh-chisel-i-dublirovaniem-soobshchenij-07-24).

    Разбор домашнего задания для *3-го вебинара*. Тема: Работа с файловой системой, чтение и запись файлов, отправка файлов ботом 
    ➡️ Разбор:[ссылка](https://telegra.ph/Domashnee-zadanie-3---Sozdanie-Telegram-bota-dlya-sozdaniya-oprosov-07-24).

    Разбор домашнего задания для *4-го вебинара*. Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests 
    ➡️ Разбор:[ссылка](https://telegra.ph/Domashnee-zadanie-4---JSON-Rabota-s-publichnymi-API-otpravka-sluchajnogo-izobrazheniya-biblioteka-requests-07-26)

    Разбор домашнего задания для *6-го вебинара*. Тема: Кнопки в боте 
    ➡️ Разбор:[ссылка](https://telegra.ph/Domashnee-zadanie-6---Knopki-v-bote-07-26)

    Разбор домашнего задания для *9-го вебинара*. Тема: Итоговый проект
    ➡️ Разбор:[ссылка](https://telegra.ph/Domashnee-zadanie-9-Itogovyj-proekt-07-29)

    Остальные материалы будут доступны по мере их разработки.

    Так же доступен [GitHub](https://github.com/MishinIgor/3modPython/tree/master) с которым мы работаем на вебинарах

    Если у вас возникли вопросы или проблемы с домашними заданиями, вот несколько советов:

    1. **Пересмотрите записи вебинаров**: Вебинары содержат много полезной информации, которая может помочь вам с выполнением домашних заданий.
    2. **Задайте вопрос в чате курса**: В чате всегда есть студенты и преподаватели, готовые помочь.
    3. **Свяжитесь с преподавателем**: Если вам нужна дополнительная помощь, не стесняйтесь обратиться к преподавателю.

    Контакты для поддержки:
    👩‍🏫 **Преподаватель:** Игорь Мишин [@Imishinigor](https://t.me/Imishinigor)
    👨‍💻 **Тьютор:** Александр Головачев [@YourBuduschee2](https://t.me/YourBuduschee2)
    🛟 **Кураторы:** Анастасия [@plastasya](https://t.me/plastasya) и Яна [@qtwec](https://t.me/qtwec)

    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад в помощь", callback_data="help")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(handle_homework_help, lambda call: call.data == "homework_help")
