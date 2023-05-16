from aiogram.types import Message, CallbackQuery, InputMediaPhoto

import Text
from Classes import User
from Keyboards import kb_start
from Keyboards.Callback import mmenu
from loader import dp, db, bot


@dp.callback_query_handler(mmenu.filter(button='main'))
@dp.message_handler(commands=['start'])
async def com_start(message: Message | CallbackQuery, user: User):
    # c_id = message.chat.id
    # m_id = message.message_id
    # my_id = message.from_user.id
    # name = message.from_user.first_name
    # max_count = settings.U_SET[my_id][1]
    # turn = settings.U_SET[my_id][2]
    poster = user.poster
    caption = Text.start(user.name, user.max_count, user.turn)
    if isinstance(message, Message):
        await bot.send_photo(chat_id=user.chat_id, photo=poster, caption=caption,
                             reply_markup=kb_start(user))
    else:
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                     chat_id=user.chat_id, message_id=user.message_id,
                                     reply_markup=kb_start(user))


@dp.message_handler(content_types=['photo'])
async def set_poster(message: Message, user: User):
    poster = message.photo[0].file_id
    db.poster(user.id, poster)
