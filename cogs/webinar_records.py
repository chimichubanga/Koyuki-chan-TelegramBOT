from aiogram import types, Dispatcher

async def handle_webinar_records(call: types.CallbackQuery):
    text = """
    **ЗАПИСИ ВЕБИНАРОВ ТРЕТЬЕГО МОДУЛЯ**

    *1 вебинар*. Тема: Знакомство с телеграмм ботами, получение токена, создание первой команды 
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240710_znakomstvo_s_tg_botami_16_00_mishin.mp4)

    *2 вебинар*. Тема: Обработка команд пользователя, работа с текстовыми сообщениями 
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240713_obrabotka_komand_16_00_mishin.mp4)

    *3 вебинар*. Тема: Работа с файловой системой, чтение и запись файлов, отправка файлов ботом 
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240715_rabota_s_faylov_mishin_16_00.mp4)

    *4 вебинар*. Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests (Часть 1)
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240719_json_rabota_s_p_mishin_16_00.mp4)

    *5 вебинар*. Тема: JSON. Работа с публичными API, отправка случайного изображения, библиотека requests (Часть 2)
    по ссылке: [ссылка](https://v.lscdn.ru/cdn7/synergy_academy/kb/wr_20240721_bot_otpravl_prognoz_pog_16_00_mish.mp4)
    """
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")]
    ])
    await call.message.edit_text(text, reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(handle_webinar_records, lambda call: call.data == "webinar_records")
