from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# Main
btn_sign_up = KeyboardButton("О нас")
btn_queshion = KeyboardButton("Задать вопрос")
btn_articles = KeyboardButton("Полезные статьи")
btn_sales = KeyboardButton("Прайс с акциями до -50%")
btn_inst = KeyboardButton("Наши работы")
btn_contacts = KeyboardButton("Наши контакты")
kb_mark_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_mark_main.add(btn_sales).row(btn_queshion, btn_inst).add(btn_articles).row(btn_sign_up, btn_contacts)

# Contacts
btn_contacts_site = InlineKeyboardButton("Сайт", url="https://www.your-clinic.pro/")
btn_contacts_tg = InlineKeyboardButton("Telegram", url="https://t.me/YourClinicMSK")
inl_kb_mark_contacts = InlineKeyboardMarkup().add(btn_contacts_tg).add(btn_contacts_site)

# Queshions
btn_tg = InlineKeyboardButton("Диалог Telegram", url="https://t.me/YourClinicMSK")
btn_num = InlineKeyboardButton("Позвонить", callback_data="call")
inl_kb_mark_queshions = InlineKeyboardMarkup().add(btn_tg).add(btn_num)

# Sign up
btn_sign_up_num = InlineKeyboardButton("По телефону", callback_data="call")
btn_sign_up_tg = InlineKeyboardButton("Telegram", url="https://t.me/YourClinicMSK")
inl_kb_mark_sign_up = InlineKeyboardMarkup().add(btn_sign_up_num).add(btn_sign_up_tg)

# Price
services = ["Брекет системы 12.990₽", "Имплантация 14.990₽", "Лечение кариеса 1.990₽", "Профессиональная гигиена 2.990₽", "Керамические виниры e-max 11.990₽", "Реставрация скола зуба 1.990₽", "Циркониевая коронка 9.990₽", "Удаление зуба 1.990₽"]
inl_kb_mark_services = InlineKeyboardMarkup()
for i, ser in enumerate(services):
    inl_kb_mark_services.add(InlineKeyboardButton(ser, callback_data=f"ser_{i+1}"))
btn_sign_up_num_2 = InlineKeyboardButton("Консультация по телефону  ☎️", callback_data="call")
btn_sign_up_tg_2 = InlineKeyboardButton("Консультация в Telegram 💬", url="https://t.me/YourClinicMSK")
inl_kb_mark_services.add(btn_sign_up_num_2).add(btn_sign_up_tg_2)
btn_sign_up_service = InlineKeyboardButton("Записаться", callback_data="sign_up")
btn_back_service = InlineKeyboardButton("Назад", callback_data="back_ser")
inl_kb_mark_service_description = InlineKeyboardMarkup().add(btn_sign_up_service).add(btn_back_service)

# Articles
articles = ['Как правильно чистить зубы?', "Как правильно выбрать зубную пасту?", 'Что делать, если болит зуб?']
inl_kb_mark_articles = InlineKeyboardMarkup()
for i, art in enumerate(articles):
    inl_kb_mark_articles.add(InlineKeyboardButton(art, callback_data=f"art_{i+1}"))
btn_back_articles = InlineKeyboardButton("Назад", callback_data="back_art")
inl_kb_mark_articles_description = InlineKeyboardMarkup().add(btn_back_articles)

# Works
works = [
    ['виниры', 'Процесс установки керамических винир.', "https://t.me/YourClinic_pro/154"], 
    ['брекеты', "Процесс установки брекет - систем.", "https://t.me/YourClinic_pro/145"], 
    ['кариес', 'Процесс лечения глубокого кариеса.', "https://t.me/YourClinic_pro/146"], 
    ['зубные импланты', 'Процесс установки зубного имплантата.', "https://t.me/YourClinic_pro/141"], 
    ['гигиеническая чистка полости рта', 'Процесс гигиенической чистки полости рта.', "https://t.me/YourClinic_pro/157"], 
]
btns_about_work = []
btns_work_tglink = []
inl_kb_mark_works = InlineKeyboardMarkup()
for i, work in enumerate(works):
    inl_kb_mark_works.add(InlineKeyboardButton(work[1], callback_data=f"work_{i+1}"))
    btns_about_work.append(InlineKeyboardButton(f"Что такое {work[0]}?", callback_data=f"what_{i+1}"))
    btns_work_tglink.append(InlineKeyboardButton("Посмотреть работы в Telegram", url=work[2]))
btn_back_works = InlineKeyboardButton("Назад", callback_data="back_work")
inl_kb_mark_what_works = InlineKeyboardMarkup().add(btn_back_works)



