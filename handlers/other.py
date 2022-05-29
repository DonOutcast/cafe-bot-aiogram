import  json, string
from aiogram import types, Dispatcher
from create_bot import dp




# @dp.message_handler()
async def clear_chat(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation and string.digits)) for i in message.text.split(' ')} \
    .intersection(set(json.load(open('swearword.json')))) != set():
        await message.reply("Нецензурная брань запрещена!!!")
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(clear_chat)