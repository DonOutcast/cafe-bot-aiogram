from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button_load = KeyboardButton('Загрузить')
button_delete = KeyboardButton('Удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)

kb_admin.add(button_load).add(button_delete)

menu_admin = InlineKeyboardMarkup(row_width=2)
button_first_dish = InlineKeyboardButton(text='Перове блюдо', callback_data='button_first_dish')
button_second_dish = InlineKeyboardButton(text='Второе', callback_data='button_second_dish')
menu_admin.add(button_first_dish)
