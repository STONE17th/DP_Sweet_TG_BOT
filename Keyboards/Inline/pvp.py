from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InKB

from Classes import User
from ..Callback import pvp_confirm


def kb_pvp_confirm(user: User):
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn_yes = InKB(text='Да', callback_data=pvp_confirm.new(confirm=user.id, button='yes'))
    btn_no = InKB(text='Нет', callback_data=pvp_confirm.new(first=user.id, button='no'))
    keyboard.row(btn_yes, btn_no)
    return keyboard
