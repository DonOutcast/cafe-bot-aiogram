from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("Режим-работы")
b2 = KeyboardButton("Расположение")
b3 = KeyboardButton("Меню")
b4 =KeyboardButton("Номер", request_contact=True)
b5 =KeyboardButton("Где я ?", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)

kb_client.add(b3).add(b1).insert(b2).row(b4,b5)