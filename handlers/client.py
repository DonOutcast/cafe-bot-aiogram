from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from database import sqlite_db

# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,"Добро пожаловать!\nЭтот бот в разработке", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом только через кнопки")

# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Этот бот еще в разработке!")
    await message.delete()

# @dp.message_handler(commands=['Режим-работы'])
async def command_working_mode(message: types.Message):
    await bot.send_message(message.from_user.id ,"Круглосуточно!")
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
    await sqlite_db.sql_read(message)


def register_handlers_clietn(dp: Dispatcher):
    dp.register_message_handler(command_start, lambda message: 'start' in message.text)
    dp.register_message_handler(command_help, lambda message: 'help' in message.text)
    dp.register_message_handler(command_working_mode, lambda message: 'Режим-работы' in message.text)
    dp.register_message_handler(command_location, lambda message: 'Расположение' in message.text)
    dp.register_message_handler(command_menu, lambda message: 'Меню' in message.text)
    dp.register_message_handler(empty)