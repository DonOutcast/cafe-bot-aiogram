from aiogram import Bot, Dispatcher
import os, config
from aiogram.contrib.fsm_storage.memory import MemoryStorage # Позваляет хранить данные в оперативное памяти
# Для созранения ответтов от пользователя
storage = MemoryStorage()

# Инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot, storage=storage)
