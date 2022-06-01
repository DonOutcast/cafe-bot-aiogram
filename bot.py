from aiogram.utils import executor
from create_bot import  dp
from database import sqlite_db


async def on_starttup(_):
    print("Бот запущен")
    sqlite_db.sql_start()

from handlers import client, admin, other
admin.register_handlers_admin(dp)
client.register_handlers_clietn(dp)
other.register_handlers_other(dp)
# Запускаем лонг поллинг

executor.start_polling(dp, skip_updates=True, on_startup=on_starttup)
