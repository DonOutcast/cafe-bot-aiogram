from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

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
b12 = KeyboardButton('Назад')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)
kb_client.add(b3).add(b1).insert(b2).row(b4,b5)

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_menu.add(b6, b7).add(b10, b11).add(b8, b9)

kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back.add(b12)