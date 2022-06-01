from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp , bot
from aiogram.dispatcher.filters import Text
from keyboards import kb_admin
from database import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_change_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Чего желаете Шеф", reply_markup=kb_admin)
    await message.delete()

# Начало диалога и загрузки пунка меню
# @dp.message_handler(commands='Загрузить', state=None)
async  def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото')

#Выход из состояния
# @dp.message_handler(state="*", commands=['Отмена'])  # * - любое состояние бота
# @dp.message_handler(Text(equals='Отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await  state.finish()
        await message.reply("Ok")

# Ловим первый ответ от пользователя
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async  with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply("Теперь введите название :")

# Ловим второй ответ от пользователя
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.reply("Введите описание :")

# Ловим третий ответ от пользователя
# @dp.message_handler(state=FSMAdmin.description)
async  def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await  FSMAdmin.next()
            await message.reply("Теперь укажите цену :")

# Ловим четверытй ответ от пользователя
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text

        await sqlite_db.sql_add_command(state)
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await state.finish()  # Выход из машинного состояния и очистка всего

@dp.callback_query_handler(lambda x: x.data and x.data.startswith("del "))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

@dp.message_handler(lambda message: 'Удалить' in message.text)
async  def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))



def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, lambda message:  'Загрузить' in message.text, state=None)
    dp.register_message_handler(cm_start, Text(equals='Загрузить', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, lambda message: 'Отмена'  in message.text, state="*")
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_change_command, lambda message: 'moderator' in message.text, is_chat_admin=True)
    dp.register_message_handler(make_change_command, Text(equals='Moderator', ignore_case=True), is_chat_admin=True)
    # dp.register_message_handler(del_callback_run, lambda x: x.data and x.data.startwith("del "))
    # dp.register_message_handler(delete_item, lambda message: 'Удалить' in message.text)
