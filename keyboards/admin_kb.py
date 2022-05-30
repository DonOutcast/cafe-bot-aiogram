from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('Загрузить')
button_delete = KeyboardButton('Удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_admin.add(button_load).add(button_delete)


