from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import  *
menu_client = InlineKeyboardMarkup()
button_buy = InlineKeyboardButton(text="Купить", callback_data="button_buy")
button_add = InlineKeyboardButton(text="Добавить  в корзину", callback_data="button_add")
menu_client.add(button_buy).add(button_add)

menu_client_with_plus_minus = InlineKeyboardMarkup()
button_plus = InlineKeyboardButton(text="Плюс", callback_data="button_plus")
button_minus = InlineKeyboardButton(text="Минус", callback_data="button_minus")
button_count = InlineKeyboardButton(text="Счёт", callback_data="button_count")
menu_client_with_plus_minus.add(button_buy).row(button_minus, button_count, button_plus).add(button_add)

def choice_button(dish_id: int, count: int = 0):
    menu_client = InlineKeyboardBuilder()
    button_plus = InlineKeyboardButton(text="Плюс", callback_data=cb_choice_for_report.new(dish_id=dish_id, choice=True))
    button_minus = InlineKeyboardButton(text="Минус", callback_data=cb_choisce_for_report.new(dish_id=dish_id, choice=False))



b1 = KeyboardButton("Режим-работы")
b2 = KeyboardButton("Расположение")
b3 = KeyboardButton("Меню")
b4 =KeyboardButton("Номер", request_contact=True)
b5 =KeyboardButton("Где я ?", request_location=True)

b6 = KeyboardButton('Первые блюда')
b7 = KeyboardButton('Вторые блюда')
b8 = KeyboardButton('Напитки')
b9 = KeyboardButton('Салаты')
b10 = KeyboardButton('Мучные изделия')
b11 = KeyboardButton('Десcерты')
b12 = KeyboardButton('Вернуться')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)
kb_client.add(b3).add(b1).insert(b2).row(b4,b5)

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_menu.add(b6, b7).add(b10, b11).add(b8, b9)

kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back.add(b12)