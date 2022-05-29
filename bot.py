from aiogram import executor
from create_bot import  dp

async def on_starttup(_):
    print("Бот запущен")
from handlers import client, admin, other

client.register_handlers_clietn(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)
# Запускаем лонг поллинг

executor.start_polling(dp, skip_updates=True, on_startup=on_starttup)
