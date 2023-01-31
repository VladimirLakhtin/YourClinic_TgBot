from aiogram.types import InputFile, InputMediaVideo
from create_bot import bot
from text import texts
import keyboard
import time

async def send_message_start(message):
    await bot.send_video(message.from_user.id, video=InputFile(path_or_bytesio="media/Video.mp4"), caption=f"{texts['start']}", reply_markup=keyboard.kb_mark_main, parse_mode="HTML")

async def send_message_contacts(message):
    photo_file = InputFile(path_or_bytesio="media/locations.jpg")
    await bot.send_photo(message.from_user.id, photo=photo_file, caption=texts["contacts"], reply_markup=keyboard.inl_kb_mark_contacts)

async def send_message_queshions(message):
    await bot.send_message(message.from_user.id, texts["queshions"], reply_markup=keyboard.inl_kb_mark_queshions)

async def send_message_sign_up(message):
    await bot.send_message(message.from_user.id, texts["sign_up"], reply_markup=keyboard.inl_kb_mark_sign_up)

async def about_us_message(message):
    await bot.send_message(message.from_user.id, texts["about_us"])

async def send_message_number(call):
    await bot.send_message(call.from_user.id, texts['tel'])

# Services
async def send_message_price(message):
    await bot.send_message(message.from_user.id, texts["price"], reply_markup=keyboard.inl_kb_mark_services)

async def edit_message_service_description(call):
    await bot.edit_message_text(
        text = texts[call.data],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=keyboard.inl_kb_mark_service_description,
        parse_mode="HTML",
    )

async def edit_message_all_services(call):
    await bot.edit_message_text(
        text=texts["price"],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=keyboard.inl_kb_mark_services,
        parse_mode="HTML",
    )

# Articles
async def send_message_article(message):
    await bot.send_message(message.from_user.id, texts["articles"], reply_markup=keyboard.inl_kb_mark_articles)

async def edit_message_article_description(call):
    await bot.edit_message_text(
        text = texts[call.data],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=keyboard.inl_kb_mark_articles_description,
        parse_mode="HTML",
    )

async def edit_message_all_articles(call):
    await bot.edit_message_text(
        text=texts["articles"],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=keyboard.inl_kb_mark_articles,
        parse_mode="HTML",
    )

# Works
async def work_message(message):
    await bot.send_video(message.from_user.id, video=InputFile(path_or_bytesio="media/Video_works.mp4"), caption=texts["work"], reply_markup=keyboard.inl_kb_mark_works, parse_mode="HTML")

async def edit_message_work_description(call):
    work_number = int(call.data[-1])
    btn_tglink = keyboard.btns_work_tglink[work_number-1]
    btn_about_work = keyboard.btns_about_work[work_number-1]
    btn_back_work = keyboard.InlineKeyboardButton("Назад", callback_data= "back_work" if work_number in [1, 2] else "back_work_caption")
    inl_kb_mark_work_description = keyboard.InlineKeyboardMarkup().add(btn_about_work).add(btn_tglink).add(btn_back_work)

    if "back" in call.data or work_number in [3, 4, 5]:
        await bot.edit_message_caption(
            caption = texts[f"work_{work_number}"],
            message_id = call.message.message_id,
            chat_id = call.message.chat.id, 
            reply_markup=inl_kb_mark_work_description,
        )
    else:
        media = InputMediaVideo(InputFile(f"media/Video_work_{work_number}.mp4"), caption=texts[f"work_{work_number}"])
        await bot.edit_message_media(
            media = media,
            message_id = call.message.message_id,
            chat_id = call.message.chat.id, 
            reply_markup=inl_kb_mark_work_description,
        )

async def edit_message_all_works(call):

    if call.data == "back_work_caption":
        await bot.edit_message_caption(
            caption = texts["work"],
            message_id = call.message.message_id,
            chat_id = call.message.chat.id, 
            reply_markup=keyboard.inl_kb_mark_works,
            # parse_mode="HTML",
        )
    else:
        media = InputMediaVideo(InputFile("media/Video_works.mp4"), caption=texts["work"])

        await bot.edit_message_media(
            media = media,
            message_id = call.message.message_id,
            chat_id = call.message.chat.id, 
            reply_markup=keyboard.inl_kb_mark_works,
        )

async def edit_message_what_work(call):
    work_number = int(call.data[-1])
    btn_back_work = keyboard.InlineKeyboardButton("Назад", callback_data=f"work_back_{work_number}")
    inl_kb_mark_what_works = keyboard.InlineKeyboardMarkup().add(btn_back_work)

    await bot.edit_message_caption(
        caption = texts[call.data],
        message_id = call.message.message_id,
        chat_id = call.message.chat.id, 
        reply_markup=inl_kb_mark_what_works,
    )


def register_handlers(dp):
    dp.register_message_handler(send_message_start, commands=["start"])
    dp.register_message_handler(send_message_contacts, lambda message: "контакты" in message.text.lower(), state=None)
    dp.register_message_handler(send_message_queshions, lambda message: "вопрос" in message.text.lower(), state=None)
    dp.register_callback_query_handler(send_message_sign_up, lambda callback: callback.data == "sign_up", state=None)
    dp.register_callback_query_handler(send_message_number, lambda callback: callback.data == "call", state=None)
    dp.register_message_handler(about_us_message, lambda message: "о нас" in message.text.lower(), state=None)

    dp.register_message_handler(send_message_price, lambda message: "прайс" in message.text.lower(), state=None)
    dp.register_callback_query_handler(edit_message_service_description, lambda callback: callback.data in [f"ser_{i}" for i in range(1, 9)], state=None)
    dp.register_callback_query_handler(edit_message_all_services, lambda callback: callback.data == "back_ser", state=None)

    dp.register_message_handler(send_message_article, lambda message: "статьи" in message.text.lower(), state=None)
    dp.register_callback_query_handler(edit_message_article_description, lambda callback: callback.data in [f"art_{i}" for i in range(1, 4)], state=None)
    dp.register_callback_query_handler(edit_message_all_articles, lambda callback: callback.data == "back_art", state=None)

    dp.register_message_handler(work_message, lambda message: "работы" in message.text.lower(), state=None)
    dp.register_callback_query_handler(edit_message_work_description, lambda callback: callback.data in [f"work_{i}" for i in range(1, 6)] or callback.data in [f"work_back_{i}" for i in range(1, 6)], state=None)
    dp.register_callback_query_handler(edit_message_all_works, lambda callback: callback.data == "back_work" or callback.data == 'back_work_caption', state=None)
    dp.register_callback_query_handler(edit_message_what_work, lambda callback: callback.data in [f"what_{i}" for i in range(1, 6)], state=None)


