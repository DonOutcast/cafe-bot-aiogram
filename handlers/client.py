from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import *
from database import sqlite_db

ID = None
# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        global  ID
        ID = message.from_user.id
        await bot.send_message(message.from_user.id,"Добро пожаловать!\nЭтот бот в разработке", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом только через кнопки")

# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Этот бот еще в разработке!", reply_markup=menu_admin)
    await message.delete()

# @dp.message_handler(commands=['Режим-работы'])
async def command_working_mode(message: types.Message):
    await bot.send_message(message.from_user.id ,"Круглосуточно!", reply_markup=menu_clietn)
    await message.delete()
# @dp.message_handler(commands=['Расположение'])
async def command_location(message: types.Message):
    await bot.send_message(message.from_user.id, "ул. Менделеева 139/1")
    await message.delete()

# @dp.messega_handler()
async def empty(message: types.Message):
    await message.answer("Такой команды нетту!", reply_markup=kb_client)
    await message.delete()

# @dp.message_handler(lambda message:  'Меню' in message.text)
async def command_menu(message: types.Message):
    await message.answer("Просмотрите меню", reply_markup=kb_menu)
    # await sqlite_db.sql_read(message)

# @dp.callback_query_handler(text="button_first_dish")
async def first_dish_command(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Первое блюдо")


# @dp.message_handler(lambda message: 'Первые блюда' in message.text)
async def command_first_dish(message: types.Message):
    await message.reply("Это первые блюда", reply_markup=kb_back)
    await sqlite_db.sql_first_dish(message)
    await message.delete()

# @dp.message_handler(lambda message: 'Вторые блюда' in message.text)
async def command_second_dish(message: types.Message):
    await message.reply("Это вторые блюда", reply_markup=kb_back)
    await sqlite_db.sql_second_dish(message)
    await message.delete()

# @dp.message_handler(lambda message: 'Напитки' in message.text)
async def command_drinks(message: types.Message):
    await message.reply(" Это напитки", reply_markup=kb_back)
    await sqlite_db.sql_drinks(message)
    await message.delete()

# @dp.message_handler(lambda message: 'Салаты' in message.text)
async def command_salad(message: types.Message):
    await message.reply("Это салаты", reply_markup=kb_back)
    await sqlite_db.sql_salad(message)
    await message.delete()

# @dp.message_handler(lambda message: 'Мучные изделия' in message.text)
async def command_flour_products(message: types.Message):
    await message.reply("Это мучные изделия", reply_markup=kb_back)
    await sqlite_db.sql_flour_products(message)
    await message.delete()

# @dp.message_handler(lambda message: 'Десcерты' in message.text)
async def command_desserts(message: types.Message):
    await message.reply("Это дессерты", reply_markup=kb_back)
    await sqlite_db.sql_desserts(message)
    await message.delete()

# @dp.message_handler(lambda message: 'Вернуться' in message.text)
async def command_back(message: types.Message):
    if message.from_user.id == ID:
        await message.reply("Возврат в основное меню", reply_markup=kb_menu)
        await message.delete()

# @dp.message_handler(lambda message: 'Оформить заказ' in message.text)
async def command_create_order(message: types.Message):
    await message.reply("Выбирите позиции из меню")
    await message.delete()

# @dp.message_handler(lambda message: "Перейти к оплате" in message.text)
async def command_pay_order(message: types.Message):
    await message.reply("Отправьте чек об оплате нашему Администратору!")
    await message.delete()

# @dp.callback_query_handler(text="button_buy")
# async def buy_command(message: types.Message):
#     await bot.send_message(message.from_user.id, "Вы нажали купить",reply_markup=menu_client_with_plus_minus)

@dp.callback_query_handler(lambda call: "button_buy" in call.data)
async def next_keyboard(call):
    await call.message.edit_reply_markup(menu_client_with_plus_minus)

def register_handlers_clietn(dp: Dispatcher):
    dp.register_message_handler(command_start, lambda message: 'start' in message.text)
    dp.register_message_handler(command_help, lambda message: 'help' in message.text)
    dp.register_message_handler(command_working_mode, lambda message: 'Режим-работы' in message.text)
    dp.register_message_handler(command_location, lambda message: 'Расположение' in message.text)
    dp.register_message_handler(command_menu, lambda message: 'Меню' in message.text)
    dp.register_message_handler(command_first_dish, lambda message: 'Первые блюда' in message.text)
    dp.register_message_handler(command_second_dish, lambda message: 'Вторые блюда' in message.text)
    dp.register_message_handler(command_drinks, lambda message: 'Напитки' in message.text)
    dp.register_message_handler(command_salad, lambda message: 'Салаты' in message.text)
    dp.register_message_handler(command_flour_products, lambda message: 'Мучные изделия' in message.text)
    dp.register_message_handler(command_desserts, lambda message: 'Десcерты' in message.text)
    dp.register_message_handler(command_back, lambda message: 'Вернуться' in message.text)
    dp.register_message_handler(command_create_order, lambda message: 'Оформить заказ' in message.text)
    dp.register_message_handler(command_pay_order, lambda message: "Перейти к оплате" in message.text)

    # dp.register_message_handler(empty)