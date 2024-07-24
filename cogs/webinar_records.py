# cogs/webinar_records.py
from telebot import types

def register_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "webinar_records")
    def handle_webinar_records(call):
        text = """
        **📚 ЗАПИСИ ВЕБИНАРОВ ТРЕТЬЕГО МОДУЛЯ**

        1️⃣ *Запись первого вебинара*
        Тема: Знакомство с телеграмм ботами, получение токена, создание первой команды
        [Посмотреть запись](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240710_znakomstvo_s_tg_botami_16_00_mishin.mp4)

        2️⃣ *Запись второго вебинара*
        Тема: Обработка команд пользователя, работа с текстовыми сообщениями
        [Посмотреть запись](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240713_obrabotka_komand_16_00_mishin.mp4)

        3️⃣ *Запись третьего вебинара*
        Тема: Работа с файловой системой, чтение и запись файлов, отправка файлов ботом
        [Посмотреть запись](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240715_rabota_s_faylov_mishin_16_00.mp4)

        4️⃣ *Запись четвертого вебинара*
        Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests (Часть 1)
        [Посмотреть запись](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240719_json_rabota_s_p_mishin_16_00.mp4)

        5️⃣ *Запись пятого вебинара*
        Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests (Часть 2)
        [Посмотреть запись](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240721_bot_otpravl_prognoz_pog_16_00_mish.mp4)
        """
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="back_to_menu")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, parse_mode='Markdown')
