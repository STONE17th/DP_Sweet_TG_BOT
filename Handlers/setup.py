from aiogram.types import InputMediaPhoto

import Text
from Classes import User
from Keyboards import kb_setup, kb_counter
from Keyboards.Callback import mmenu, setup
from loader import dp, db, bot


@dp.callback_query_handler(mmenu.filter(button='setup'))
async def main_setup(_, user: User):
    poster = user.poster
    caption = Text.main(user.max_count, user.turn)
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id,
                                 reply_markup=kb_setup(user))


@dp.callback_query_handler(setup.filter(button='count'))
@dp.callback_query_handler(setup.filter(button='turn'))
async def counter(_, user: User):
    _, button, count = user.data
    db.setup(user.id, button, count)
    user.refresh()
    poster = user.poster
    caption = Text.count(user.max_count) if button == 'count' else Text.turn(user.turn)
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id,
                                 reply_markup=kb_counter(button, int(count), user))
