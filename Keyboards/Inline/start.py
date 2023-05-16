from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

import settings
from Classes import User
from ..Callback import mmenu


def kb_start(user: User):
    keyboard = InlineKeyboardMarkup(row_width=3)
    text_pvp = 'PVP: ✅' if user.id in settings.pvp_waiting_list else 'PVP: ❎'
    text_start = 'new_pvp' if user.id in settings.pvp_waiting_list else 'new_game'
    btn_start = InKB(text='Начать', callback_data=mmenu.new(button=text_start))
    btn_setup = InKB(text='Настройки', callback_data=mmenu.new(button='setup'))
    btn_pvp = InKB(text=text_pvp, callback_data=mmenu.new(button='pvp'))

    keyboard.row(btn_start, btn_setup, btn_pvp)
    return keyboard


def kb_end_game(bot: bool = False):
    keyboard = InlineKeyboardMarkup(row_width=3)
    if bot:
        return keyboard
    btn_again = InKB(text='Еше раз', callback_data=mmenu.new(button='new_game'))
    btn_main = InKB(text='В меню', callback_data=mmenu.new(button='main'))

    keyboard.row(btn_again, btn_main)
    return keyboard
