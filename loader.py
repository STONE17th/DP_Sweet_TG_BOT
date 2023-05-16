from os import getenv

from aiogram import Bot, Dispatcher

from Database import DataBase

battle_list = {}

db = DataBase()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot)
