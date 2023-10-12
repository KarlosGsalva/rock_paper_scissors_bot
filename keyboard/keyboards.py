from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# --------- создание клавиатуры через ReplyKeyboardBuilder ------------

# создаем кнопки с ответами: согласие, отказ
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# инициализируем билдер для клавиатуры с отказом и согласием
yes_no_kb_builder = ReplyKeyboardBuilder()

# добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# создаем клавиатуру с кнопками "Давай!" и "Не хочу"!
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# --------- создание клавиатуры без билдера ------------

# создаем кнопки игровой клавиатуры
button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])

# создаем клавиатуру с кнопками "камень, ножницы, бумага"
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_rock], [button_scissors],
              [button_paper]], resize_keyboard=True)



