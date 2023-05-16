import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Classes import User
from ..Callback import take


def kb_take(target: str, count: int, user: User):
    keyboard = InlineKeyboardMarkup(row_width=5)
    shift = ['-10', '-1', '+1', '+10']

    def true_count(cnt: str | int, shift: str, user: User) -> int:
        true_cnt = int(cnt) + int(shift)
        if true_cnt > user.turn:
            return user.turn
        elif true_cnt < 1:
            return 1
        return true_cnt

    btn_counter = [InKB(text=item, callback_data=take.new(button=target, count=true_count(count, item, user))) for item
                   in shift]
    btn_random = InKB(text='RANDOM', callback_data=take.new(button=target, count=(random.randint(1, user.turn))))
    btn_take = InKB(text=f'Взять {count}', callback_data=take.new(button='take', count=count))
    keyboard.row(*btn_counter[:2], btn_random, *btn_counter[2:])
    keyboard.row(btn_take)
    return keyboard
