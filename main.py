from aiogram.utils import executor

import Middleware
from Handlers import dp
from loader import db


async def on_start(_):
    print('Бот запущен!')
    print('База данных ', end='')
    try:
        db.create_table()
        print('ОК!')
    except:
        print('ОШИБКА!!!')


if __name__ == '__main__':
    Middleware.setup(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
