from aiogram import Dispatcher, Bot
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
GROUP_ID = config("GROUP_ID")
GROUP_ID2 = config("GROUP_ID2")
ADMIN_ID = config("ADMIN_ID")
MEDIA = config("MEDIA")
