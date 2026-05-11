import telebot
from telebot import types
import time

BOT_TOKEN = '8516458401:AAFHetGV-0ygbu5f0nG7boDzvg5vx6nbrgE'

bot = telebot.TeleBot(BOT_TOKEN)

# ===== ТЕКСТЫ =====

TEXTS = {
    "fake_hallmarks": "🔍 *Поддельные клейма*\n\nКлеймо — главный признак подлинности ювелирного изделия. Признаки подделки:\n\n• Клеймо нанесено криво или нечётко\n• Цифры пробы размыты или плохо читаются\n• Клеймо нанесено поверх узора, а не до него\n• Отсутствует клеймо пробирной палаты\n• На изделии только иностранные клейма (LV, TR) без российского клейма\n\n✅ Настоящее клеймо: чёткий штамп, ровные края, нанесено до декора изделия.",
    "bad_materials": "⚠️ *Некачественные материалы*\n\nПризнаки использования дешёвых материалов:\n\n• Зеленоватый или чёрный след на коже — признак меди или мельхиора\n• Золотое покрытие облезает на краях и выступах\n• Изделие слишком лёгкое для своего размера\n• Металл царапается ногтем — много свинца в составе\n• При сгибании тонких цепочек металл трескается\n\n✅ Настоящее золото 585 пробы не оставляет следов на коже и не царапается ногтем.",
    "check_yourself": "🔎 *Как проверить самому*\n\nПростые тесты в домашних условиях:\n\n1. *Магнит* — золото и серебро не магнитятся. Если изделие притягивается — внутри стальная основа\n\n2. *Вес* — золото очень тяжёлое (19,3 г/см³). Подделка того же размера будет заметно легче\n\n3. *Уксус* — нанесите каплю на незаметное место. Настоящее золото не реагирует, подделка темнеет\n\n4. *Лупа* — осмотрите клеймо. Оно должно быть чётким, без размытий\n\n5. *Ноготь* — проведите ногтем. Царапина остаётся только на очень мягких подделках\n\n⚠️ Для точного результата обратитесь к сертифицированному эксперту.",
    "what_is_hallmark": "💎 *Что такое проба?*\n\nПроба — это цифровое обозначение содержания драгоценного металла в сплаве на 1000 частей.\n\n*Золото:*\n• 999 — чистое золото (мягкое, используется в слитках)\n• 750 — 75% золота (белое, жёлтое, розовое золото)\n• 585 — 58,5% золота (самая популярная в России)\n• 375 — 37,5% золота (бюджетные украшения)\n\n*Серебро:*\n• 999 — чистое серебро\n• 925 — Sterling Silver (самая популярная)\n• 875 — советский стандарт\n• 830 — столовое серебро\n\n*Платина:*\n• 950 — 95% платины\n• 850 — 85% платины",
    "hallmark_decode": "🏷 *Расшифровка клейм*\n\nНа российских ювелирных изделиях обязательно должны быть:\n\n1. *Клеймо пробирной палаты* — женская голова в кокошнике + цифра пробы\n\n2. *Именник производителя* — буквенный код завода-изготовителя\n\n3. *Проба* — цифровое обозначение (375, 585, 750, 925 и др.)\n\n*Иностранные клейма:*\n• 14K = 585 проба\n• 18K = 750 проба\n• 925 = серебро Sterling\n• 750 IT = итальянское золото 750 пробы\n\n⚠️ Изделия только с иностранными клеймами без российского клейма не считаются легальными на рынке РФ.",
    "gost_hallmark": "📋 *ГОСТ 30632-2014*\n\nГосударственный стандарт на ювелирные изделия из драгоценных металлов.\n\n*Основные требования:*\n• Все ювелирные изделия из драгметаллов обязаны иметь клеймо государственной пробирной палаты\n• Клеймо наносится до финальной обработки изделия\n• Проба должна соответствовать фактическому содержанию металла\n• Отклонение от пробы допускается не более ±3 единиц\n\nСайт: probpalata.gov.ru",
    "natural_vs_synthetic": "✨ *Натуральные vs синтетические камни*\n\n*Натуральные камни:*\n• Образуются в природе миллионы лет\n• Имеют уникальные включения и дефекты\n• Стоят значительно дороже\n• Ценность растёт со временем\n\n*Синтетические камни:*\n• Выращены в лаборатории\n• Химически идентичны натуральным\n• Стоят в 10-20 раз дешевле\n• Должны маркироваться как синтетические\n\n*Имитации:*\n• Фианит — имитация бриллианта\n• Стекло — имитация любого камня\n\n✅ Требуйте у продавца геммологический сертификат на камень.",
    "diamonds": "💍 *Бриллианты*\n\nБриллиант — это огранённый алмаз. Качество оценивается по системе 4C:\n\n*1. Carat (Карат) — вес*\n• 1 карат = 0,2 грамма\n\n*2. Cut (Огранка)*\n• Excellent — идеальная\n• Very Good — очень хорошая\n• Good — хорошая\n\n*3. Color (Цвет)*\n• D-F — бесцветные (самые дорогие)\n• G-J — почти бесцветные\n• K-Z — с оттенком\n\n*4. Clarity (Чистота)*\n• FL/IF — без включений\n• VVS1-VVS2 — минимальные включения\n• VS1-VS2 — небольшие включения\n\n✅ Настоящий бриллиант царапает стекло.",
    "popular_stones": "💎 *Популярные камни*\n\n🔴 *Рубин* — красный корунд. Натуральные дороже бриллиантов.\n\n🔵 *Сапфир* — синий корунд. Бывает разных цветов.\n\n💚 *Изумруд* — разновидность берилла. Включения — норма.\n\n💜 *Аметист* — фиолетовый кварц. Синтетические почти неотличимы визуально.\n\n⚪ *Жемчуг* — натуральный тёплый и шершавый, искусственный холодный и гладкий.\n\n🩵 *Бирюза* — часто продают прессованную или крашеную.",
    "gost_gold": "📜 *ГОСТ на золото*\n\n📌 *ГОСТ Р 51152-98* — Золото в ювелирных изделиях\n• Допустимые пробы: 375, 500, 585, 750, 958, 999\n• Допуск отклонения: ±3 единицы от указанной пробы\n\n📌 *ГОСТ 6835-2002* — Золото и сплавы на его основе\n• Химический состав сплавов\n• Механические свойства\n• Методы испытаний\n\n📌 *Технический регламент ЕАЭС 051/2021*\n• Требования к маркировке\n• Правила оборота ювелирных изделий в ЕАЭС\n\n🌐 probpalata.gov.ru",
    "gost_silver": "📜 *ГОСТ на серебро*\n\n📌 *ГОСТ Р 51152-98* — Серебро в ювелирных изделиях\n• Допустимые пробы: 800, 830, 875, 925, 960, 999\n• Самая распространённая — 925 (Sterling Silver)\n• Допуск отклонения: ±3 единицы\n\n📌 *ГОСТ 6836-2002* — Серебро и сплавы на его основе\n\n*Пробы серебра:*\n• 999 — чистое серебро\n• 925 — Sterling, самое популярное\n• 875 — советский стандарт\n• 800 — низкопробное, быстро темнеет\n\n*Уход:*\nСеребро темнеет от серы и влаги. Чистить мягкой тканью.",
    "gost_diamonds": "📜 *ГОСТ на бриллианты*\n\n📌 *ГОСТ Р 52913-2008* — Бриллианты. Классификация.\n\n*Классификация по массе:*\n• Мелкие — до 0,29 карата\n• Средние — 0,30 — 0,99 карата\n• Крупные — от 1,00 карата\n\n*Группы цвета (1-9):*\n• 1-2 — бесцветные (высшая категория)\n• 3-5 — с едва заметным оттенком\n• 8-9 — с явным оттенком\n\n*Группы чистоты (1-9):*\n• 1 — без включений\n• 2-3 — с мельчайшими включениями\n• 6-9 — с крупными включениями\n\n*Сертификация:*\nБриллианты от 0,30 карата должны иметь сертификат ГИА, IGI или АГС.",
    "find_expert": "👨‍💼 *Как найти сертифицированного эксперта*\n\n*Где искать:*\n• Государственные пробирные инспекции\n• Геммологические центры при ювелирных заводах\n• Независимые геммологи с сертификатом ГИА или IGI\n\n*На что обратить внимание:*\n• Диплом геммолога (ГИА, IGI, ГГО)\n• Официальный договор на экспертизу\n• Письменное заключение с печатью\n\n*Средняя стоимость:*\n• Определение металла и пробы — от 500 руб.\n• Оценка камней — от 1000 руб. за камень\n• Полная экспертиза — от 2000 руб.\n\n🌐 probpalata.gov.ru\n📞 8-800-511-00-89 (бесплатно)",
}

# ===== ЧЕКЛИСТ =====

CHECKLIST = [
    {
        "question": "1️⃣ Есть ли на украшении клеймо пробирной палаты?\n\n💡 *Подсказка:* Это небольшой штамп с изображением женской головы в кокошнике и цифрой пробы (например 585, 750, 925).",
        "critical": True
    },
    {
        "question": "2️⃣ Клеймо чёткое и хорошо читается?\n\n💡 *Подсказка:* Настоящее клеймо имеет ровные края и чёткие цифры. Размытое или кривое клеймо — признак подделки.",
        "critical": True
    },
    {
        "question": "3️⃣ Есть ли именник производителя рядом с клеймом?\n\n💡 *Подсказка:* Это буквенный код завода-изготовителя (например ЯЮ, МФ). Должен быть рядом с пробой.",
        "critical": False
    },
    {
        "question": "4️⃣ Украшение не притягивается к магниту?\n\n💡 *Подсказка:* Золото и серебро не магнитятся. Если магнитится — внутри стальная основа под тонким покрытием.",
        "critical": True
    },
    {
        "question": "5️⃣ Вес украшения соответствует его размеру?\n\n💡 *Подсказка:* Возьмите в руку — золото тяжёлое. Если кольцо или цепочка кажутся слишком лёгкими для своего размера — это подозрительно.",
        "critical": False
    },
    {
        "question": "6️⃣ Нет следов облезающего или отслаивающегося покрытия?\n\n💡 *Подсказка:* Осмотрите края, застёжки и выступающие части. Облезание говорит о дешёвом металле под тонким золотым покрытием.",
        "critical": True
    },
    {
        "question": "7️⃣ Продавец готов выдать товарный чек с характеристиками?\n\n💡 *Подсказка:* В чеке должны быть указаны: металл, проба, вес, вставки. Отказ выдать чек — серьёзный красный флаг.",
        "critical": True
    },
    {
        "question": "8️⃣ Если в украшении есть камни — есть сертификат на них?\n\n💡 *Подсказка:* Для бриллиантов от 0.3 карата обязателен сертификат ГИА или IGI. Если камней нет — нажмите ✅.",
        "critical": False
    },
]

# ===== ТЕСТ =====

QUIZ = [
    {
        "question": "💍 Кольцо из жёлтого металла. На нём стоит клеймо 585 с женской головой в кокошнике и именник завода. Цвет не меняется, следов на коже нет.",
        "answer": "original",
        "explanation": "✅ Это *оригинал*. Клеймо пробирной палаты + проба 585 + именник завода — все три обязательных элемента на месте."
    },
    {
        "question": "⌚ Браслет. На нём выбито только '14K' без других клейм. При ношении оставляет зеленоватый след на коже.",
        "answer": "fake",
        "explanation": "❌ Это *подделка*. Только иностранное клеймо без российского — нарушение. Зелёный след говорит о меди или мельхиоре под тонким покрытием."
    },
    {
        "question": "💎 Кольцо с бриллиантом. Продавец говорит что камень натуральный, но сертификата нет. Камень идеально прозрачный, без единого включения.",
        "answer": "fake",
        "explanation": "❌ Скорее всего *подделка* или синтетика. Натуральные бриллианты почти всегда имеют микровключения. Идеальная чистота без сертификата — повод для подозрений."
    },
    {
        "question": "🔗 Золотая цепочка. Клеймо чёткое, проба 585. Вес соответствует размеру. При тесте магнитом — не реагирует.",
        "answer": "original",
        "explanation": "✅ Это *оригинал*. Чёткое клеймо, правильная проба, соответствующий вес и отсутствие реакции на магнит — все признаки подлинного золота."
    },
    {
        "question": "💍 Серебряное кольцо с пробой 925. Но при ношении буквально за неделю почернело полностью и оставило тёмный след на пальце.",
        "answer": "fake",
        "explanation": "❌ Это *подделка*. Настоящее серебро 925 темнеет медленно. Быстрое почернение и следы на коже — признак дешёвого сплава."
    },
    {
        "question": "💎 Кольцо с рубином. Камень насыщенного красного цвета, идеально равномерный, без каких-либо включений. Цена — 3000 рублей.",
        "answer": "fake",
        "explanation": "❌ Это *подделка* или синтетика. Натуральные рубины без включений стоят тысячи долларов. Идеальный цвет + низкая цена = синтетика или стекло."
    },
    {
        "question": "🏅 Золотой кулон 750 пробы. Клеймо чёткое, именник есть. Изделие заметно легче чем должно быть для своего размера.",
        "answer": "fake",
        "explanation": "❌ Это *подделка*. Несмотря на клейма, подозрительно малый вес говорит о пустотах внутри или покрытии поверх дешёвого металла."
    },
    {
        "question": "💍 Обручальное кольцо. На внутренней стороне чёткое клеймо 585, женская голова, именник. Не магнитится, вес нормальный, следов на коже нет.",
        "answer": "original",
        "explanation": "✅ Это *оригинал*. Все признаки подлинности присутствуют: правильное клеймо, нет реакции на магнит, нормальный вес, нет следов на коже."
    },
]

user_quiz_state = {}
user_checklist_state = {}
user_shop_check = {}


# ===== МЕНЮ =====

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("🔍 Признаки фальсификации"),
        types.KeyboardButton("💎 Проба и маркировка"),
        types.KeyboardButton("✨ Качество камней"),
        types.KeyboardButton("📜 ГОСТы и стандарты"),
        types.KeyboardButton("👨‍💼 Найти эксперта"),
        types.KeyboardButton("🏪 Проверить магазин"),
        types.KeyboardButton("📋 Чеклист при покупке"),
        types.KeyboardButton("🎮 Тест: Подделка или оригинал?")
    )
    return markup


def back_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.KeyboardButton("🔙 Главное меню"))
    return markup


def quiz_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("✅ Оригинал"),
        types.KeyboardButton("❌ Подделка")
    )
    return markup


def checklist_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("✅ Да"),
        types.KeyboardButton("❌ Нет")
    )
    markup.add(types.KeyboardButton("🔙 Отменить проверку"))
    return markup


# ===== /start =====

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я помогу разобраться в ювелирных украшениях.\n\nВыберите раздел:",
        reply_markup=main_menu()
    )


# ===== ПРИЗНАКИ ФАЛЬСИФИКАЦИИ =====

@bot.message_handler(func=lambda m: m.text == "🔍 Признаки фальсификации")
def falsification(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(
        types.KeyboardButton("🔍 Поддельные клейма"),
        types.KeyboardButton("🔍 Некачественные материалы"),
        types.KeyboardButton("🔍 Как проверить самому"),
        types.KeyboardButton("🔙 Главное меню")
    )
    bot.send_message(message.chat.id, "Выберите тему:", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "🔍 Поддельные клейма")
def fake_hallmarks(message):
    bot.send_message(message.chat.id, TEXTS["fake_hallmarks"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "🔍 Некачественные материалы")
def bad_materials(message):
    bot.send_message(message.chat.id, TEXTS["bad_materials"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "🔍 Как проверить самому")
def check_yourself(message):
    bot.send_message(message.chat.id, TEXTS["check_yourself"], parse_mode="Markdown", reply_markup=back_menu())


# ===== ПРОБА И МАРКИРОВКА =====

@bot.message_handler(func=lambda m: m.text == "💎 Проба и маркировка")
def hallmark(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(
        types.KeyboardButton("💎 Что такое проба?"),
        types.KeyboardButton("💎 Расшифровка клейм"),
        types.KeyboardButton("💎 ГОСТ 30632-2014"),
        types.KeyboardButton("🔙 Главное меню")
    )
    bot.send_message(message.chat.id, "Выберите тему:", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "💎 Что такое проба?")
def what_is_hallmark(message):
    bot.send_message(message.chat.id, TEXTS["what_is_hallmark"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "💎 Расшифровка клейм")
def hallmark_decode(message):
    bot.send_message(message.chat.id, TEXTS["hallmark_decode"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "💎 ГОСТ 30632-2014")
def gost_hallmark(message):
    bot.send_message(message.chat.id, TEXTS["gost_hallmark"], parse_mode="Markdown", reply_markup=back_menu())


# ===== КАЧЕСТВО КАМНЕЙ =====

@bot.message_handler(func=lambda m: m.text == "✨ Качество камней")
def stones(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(
        types.KeyboardButton("✨ Натуральные vs синтетические"),
        types.KeyboardButton("✨ Бриллианты"),
        types.KeyboardButton("✨ Популярные камни"),
        types.KeyboardButton("🔙 Главное меню")
    )
    bot.send_message(message.chat.id, "Выберите тему:", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "✨ Натуральные vs синтетические")
def natural_vs_synthetic(message):
    bot.send_message(message.chat.id, TEXTS["natural_vs_synthetic"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "✨ Бриллианты")
def diamonds(message):
    bot.send_message(message.chat.id, TEXTS["diamonds"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "✨ Популярные камни")
def popular_stones(message):
    bot.send_message(message.chat.id, TEXTS["popular_stones"], parse_mode="Markdown", reply_markup=back_menu())


# ===== ГОСТЫ =====

@bot.message_handler(func=lambda m: m.text == "📜 ГОСТы и стандарты")
def gosts(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(
        types.KeyboardButton("📜 ГОСТ на золото"),
        types.KeyboardButton("📜 ГОСТ на серебро"),
        types.KeyboardButton("📜 ГОСТ на бриллианты"),
        types.KeyboardButton("🔙 Главное меню")
    )
    bot.send_message(message.chat.id, "Выберите тему:", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "📜 ГОСТ на золото")
def gost_gold(message):
    bot.send_message(message.chat.id, TEXTS["gost_gold"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "📜 ГОСТ на серебро")
def gost_silver(message):
    bot.send_message(message.chat.id, TEXTS["gost_silver"], parse_mode="Markdown", reply_markup=back_menu())


@bot.message_handler(func=lambda m: m.text == "📜 ГОСТ на бриллианты")
def gost_diamonds(message):
    bot.send_message(message.chat.id, TEXTS["gost_diamonds"], parse_mode="Markdown", reply_markup=back_menu())


# ===== НАЙТИ ЭКСПЕРТА =====

@bot.message_handler(func=lambda m: m.text == "👨‍💼 Найти эксперта")
def find_expert(message):
    bot.send_message(message.chat.id, TEXTS["find_expert"], parse_mode="Markdown", reply_markup=back_menu())


# ===== ПРОВЕРИТЬ МАГАЗИН =====

@bot.message_handler(func=lambda m: m.text == "🏪 Проверить магазин")
def check_shop(message):
    user_shop_check[message.chat.id] = True
    bot.send_message(
        message.chat.id,
        "🏪 *Проверка магазина*\n\nНапишите название магазина или ювелирной сети:",
        parse_mode="Markdown",
        reply_markup=back_menu()
    )


@bot.message_handler(func=lambda m: m.chat.id in user_shop_check and user_shop_check.get(m.chat.id) and m.text != "🔙 Главное меню")
def process_shop_check(message):
    shop_name = message.text
    del user_shop_check[message.chat.id]
    response = f"🏪 *Как проверить магазин \"{shop_name}\"*\n\n*Шаг 1 — Реестр Пробирной палаты*\nПроверьте есть ли магазин в официальном реестре:\n🌐 probpalata.gov.ru/registries\n\n*Шаг 2 — Проверка юридического лица*\nНайдите ИНН магазина на чеке и проверьте:\n🌐 egrul.nalog.ru\n\n*Шаг 3 — Отзывы покупателей*\n• Яндекс Карты\n• 2ГИС\n• Otzovik.com\n• Irecommend.ru\n\n*Шаг 4 — Красные флаги* ⚠️\nНе покупайте если:\n• Нет кассового аппарата\n• Отказывают в товарном чеке\n• Нет сертификатов на камни\n• Давят на срочность покупки\n• Цена подозрительно низкая\n\n*Шаг 5 — В самом магазине*\n• Попросите документы на товар\n• Проверьте клеймо через лупу\n• Убедитесь что дают гарантийный талон\n\n✅ Надёжный магазин всегда предоставит все документы без вопросов."
    bot.send_message(message.chat.id, response, parse_mode="Markdown", reply_markup=main_menu())


# ===== ЧЕКЛИСТ =====

@bot.message_handler(func=lambda m: m.text == "📋 Чеклист при покупке")
def start_checklist(message):
    user_id = message.chat.id
    user_checklist_state[user_id] = {
        "question": 0,
        "yes_count": 0,
        "no_critical": False,
        "answers": []
    }
    bot.send_message(
        user_id,
        "📋 *Чеклист при покупке украшения*\n\nОтвечайте на вопросы прямо в магазине. В конце я скажу — безопасно покупать или нет.\n\nПоехали! 👇",
        parse_mode="Markdown"
    )
    time.sleep(1)
    send_checklist_question(user_id)


def send_checklist_question(user_id):
    state = user_checklist_state[user_id]
    q_index = state["question"]
    if q_index >= len(CHECKLIST):
        finish_checklist(user_id)
        return
    question = CHECKLIST[q_index]
    num = q_index + 1
    total = len(CHECKLIST)
    bot.send_message(
        user_id,
        f"*Вопрос {num} из {total}:*\n\n{question['question']}",
        parse_mode="Markdown",
        reply_markup=checklist_menu()
    )


@bot.message_handler(func=lambda m: m.text in ["✅ Да", "❌ Нет"] and m.chat.id in user_checklist_state)
def handle_checklist_answer(message):
    user_id = message.chat.id
    state = user_checklist_state[user_id]
    q_index = state["question"]
    question = CHECKLIST[q_index]
    answered_yes = message.text == "✅ Да"
    if answered_yes:
        state["yes_count"] += 1
    else:
        if question["critical"]:
            state["no_critical"] = True
    state["answers"].append(answered_yes)
    state["question"] += 1
    if state["question"] >= len(CHECKLIST):
        finish_checklist(user_id)
    else:
        send_checklist_question(user_id)


def finish_checklist(user_id):
    state = user_checklist_state[user_id]
    yes_count = state["yes_count"]
    no_critical = state["no_critical"]
    total = len(CHECKLIST)
    if no_critical:
        verdict = "🔴 *НЕ ПОКУПАЙТЕ это украшение!*\n\nВы ответили «Нет» на один из критически важных вопросов. Это серьёзный признак подделки."
        advice = "💡 Попросите продавца объяснить несоответствия. Если не может — уходите."
    elif yes_count == total:
        verdict = "🟢 *Украшение выглядит надёжно!*\n\nВсе пункты проверки пройдены успешно."
        advice = "💡 Не забудьте взять товарный чек и сохранить его."
    elif yes_count >= 6:
        verdict = "🟡 *Покупайте осторожно.*\n\nБольшинство пунктов в порядке, но есть небольшие сомнения."
        advice = "💡 Попросите дополнительные документы на товар."
    else:
        verdict = "🔴 *НЕ ПОКУПАЙТЕ это украшение!*\n\nСлишком много подозрительных признаков."
        advice = "💡 Обратитесь в другой магазин или к сертифицированному эксперту."
    bot.send_message(
        user_id,
        f"📋 *Проверка завершена!*\n\nВаш результат: *{yes_count} из {total}* ✅\n\n{verdict}\n\n{advice}",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )
    del user_checklist_state[user_id]


@bot.message_handler(func=lambda m: m.text == "🔙 Отменить проверку")
def cancel_checklist(message):
    user_id = message.chat.id
    if user_id in user_checklist_state:
        del user_checklist_state[user_id]
    bot.send_message(user_id, "Проверка отменена.", reply_markup=main_menu())


# ===== ТЕСТ =====

@bot.message_handler(func=lambda m: m.text == "🎮 Тест: Подделка или оригинал?")
def start_quiz(message):
    user_id = message.chat.id
    user_quiz_state[user_id] = {"question": 0, "score": 0, "answers": []}
    bot.send_message(
        user_id,
        "🎮 *Тест: Подделка или оригинал?*\n\nЯ опишу украшение, а вы определите — оригинал это или подделка.\n\nВсего 8 вопросов. Удачи! 🍀",
        parse_mode="Markdown"
    )
    send_quiz_question(user_id)


def send_quiz_question(user_id):
    state = user_quiz_state[user_id]
    q_index = state["question"]
    if q_index >= len(QUIZ):
        finish_quiz(user_id)
        return
    question = QUIZ[q_index]
    num = q_index + 1
    total = len(QUIZ)
    bot.send_message(
        user_id,
        f"*Вопрос {num} из {total}:*\n\n{question['question']}",
        parse_mode="Markdown",
        reply_markup=quiz_menu()
    )


@bot.message_handler(func=lambda m: m.text in ["✅ Оригинал", "❌ Подделка"] and m.chat.id in user_quiz_state)
def handle_quiz_answer(message):
    user_id = message.chat.id
    if user_id not in user_quiz_state:
        bot.send_message(user_id, "Нажмите кнопку теста чтобы начать.", reply_markup=main_menu())
        return
    state = user_quiz_state[user_id]
    q_index = state["question"]
    question = QUIZ[q_index]
    user_answer = "original" if message.text == "✅ Оригинал" else "fake"
    correct = user_answer == question["answer"]
    if correct:
        state["score"] += 1
        result_text = "✅ Правильно!"
    else:
        result_text = "❌ Неправильно!"
    state["answers"].append(correct)
    state["question"] += 1
    bot.send_message(user_id, f"{result_text}\n\n{question['explanation']}", parse_mode="Markdown")
    time.sleep(1)
    if state["question"] >= len(QUIZ):
        finish_quiz(user_id)
    else:
        send_quiz_question(user_id)


def finish_quiz(user_id):
    state = user_quiz_state[user_id]
    score = state["score"]
    total = len(QUIZ)
    if score == total:
        grade = "🏆 Эксперт-геммолог! Вы профессионал!"
    elif score >= 6:
        grade = "🥈 Отличный результат! Вы хорошо разбираетесь в ювелирке."
    elif score >= 4:
        grade = "🥉 Неплохо! Но есть что изучить."
    else:
        grade = "📚 Рекомендуем изучить разделы бота — там много полезного!"
    bot.send_message(
        user_id,
        f"🎮 *Тест завершён!*\n\nВаш результат: *{score} из {total}*\n\n{grade}",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )
    del user_quiz_state[user_id]


# ===== ГЛАВНОЕ МЕНЮ =====

@bot.message_handler(func=lambda m: m.text == "🔙 Главное меню")
def go_back(message):
    user_id = message.chat.id
    if user_id in user_quiz_state:
        del user_quiz_state[user_id]
    if user_id in user_checklist_state:
        del user_checklist_state[user_id]
    if user_id in user_shop_check:
        del user_shop_check[user_id]
    bot.send_message(user_id, "Выберите раздел:", reply_markup=main_menu())


# ===== ЗАПУСК =====

print("Бот запущен...")
while True:
    try:
        bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)
    except Exception as e:
        print("Ошибка соединения, перезапуск:", str(e))
        time.sleep(5)
