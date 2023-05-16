import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Classes import User
from ..Callback import mmenu, setup


def kb_setup(user: User):
    keyboard = InlineKeyboardMarkup(row_width=3)
    btn_max = InKB(text='Всего конфет', callback_data=setup.new(button='count', count=user.max_count))
    btn_turn = InKB(text='За ход', callback_data=setup.new(button='turn', count=user.turn))
    btn_back = InKB(text='Назад', callback_data=mmenu.new(button='main'))

    keyboard.row(btn_max, btn_turn)
    keyboard.row(btn_back)
    return keyboard


def kb_counter(target: str, count: int, user: User):
    keyboard = InlineKeyboardMarkup(row_width=5)
    shift = ['-10', '-1', '+1', '+10']
    btn_counter = [InKB(text=item, callback_data=setup.new(button=target, count=(int(count) + int(item)))) for item in
                   shift]
    btn_random = InKB(text='RANDOM',
                      callback_data=setup.new(button=target, count=(random.randint(1, user.max_count // 10))))
    btn_confirm = InKB(text='OK', callback_data=mmenu.new(button='setup'))
    keyboard.row(*btn_counter[:2], btn_random, *btn_counter[2:])
    keyboard.row(btn_confirm)
    return keyboard
