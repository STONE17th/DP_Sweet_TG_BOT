from aiogram import Dispatcher

from .middleware import AddSuperData


def setup(dp: Dispatcher):
    dp.middleware.setup(AddSuperData())
