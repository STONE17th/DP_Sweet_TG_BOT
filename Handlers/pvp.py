import random

from aiogram.types import CallbackQuery, InputMediaPhoto

import Text
import settings
from Classes import User
from Keyboards import kb_start, kb_pvp_confirm
from Keyboards.Callback import mmenu
from loader import dp, bot


@dp.callback_query_handler(mmenu.filter(button='pvp'))
async def bot_turn(call: CallbackQuery, user: User):
    if user.id not in settings.pvp_waiting_list:
        caption = Text.join_pvp(user.name)
        settings.pvp_waiting_list.add(user.id)
        await call.answer('Надерем задницу!!')
    else:
        caption = Text.un_join_pvp(user.name)
        settings.pvp_waiting_list.remove(user.id)
        await call.answer('Чё, зассал?')
    poster = user.poster
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id,
                                 reply_markup=kb_start(user))


@dp.callback_query_handler(mmenu.filter(button='new_pvp'))
async def bot_turn(call: CallbackQuery, user: User):
    def choose_enemy():
        while True:
            enemy_id = random.choice(settings.pvp_waiting_list)
            if user.id != enemy_id:
                return enemy_id

    if len(settings.pvp_waiting_list) > 1:
        enemy_id = choose_enemy()
    else:
        await call.answer('Ждем оппонента!', show_alert=True)
        return None
    await bot.send_message(chat_id=enemy_id, text=f'{user.name} бросает тебе вызов\nПринять?',
                           reply_markup=kb_pvp_confirm(user))
