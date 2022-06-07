from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button_load = KeyboardButton('Загрузить')
button_delete = KeyboardButton('Удалить')
button_fixed = KeyboardButton('Изменить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)

kb_admin.add(button_load).add(button_delete).add(button_fixed)

menu_admin = InlineKeyboardMarkup(row_width=2)
button_first_dish = InlineKeyboardButton(text='Перове блюдо', callback_data='button_first_dish')
button_second_dish = InlineKeyboardButton(text='Второе блюдо', callback_data='button_second_dish')
button_flour_products =InlineKeyboardButton(text='Мучное изделие', callback_data="button_flour_products")
button_drinks = InlineKeyboardButton(text='Напики' , callback_data='button_drinks')
button_salad = InlineKeyboardButton(text='Салат' , callback_data='button_salad')
button_dessert = InlineKeyboardButton(text='Дессерт' , callback_data='button_dessert')
menu_admin.add(button_first_dish, button_second_dish).add(button_flour_products, button_dessert).add(button_salad, button_drinks)
