import asyncio
import random

from aiogram.types import CallbackQuery, InputMediaPhoto

import Text
from Classes import User
from Keyboards import kb_end_game, kb_take
from Keyboards.Callback import mmenu, take
from loader import dp, bot, battle_list


async def bot_turn(call: CallbackQuery, user: User):
    bot_take = int(battle_list[user.id][0]) % int(battle_list[user.id][1])
    bot_take = bot_take if bot_take else random.randint(1, user.turn)
    battle_list[user.id][0] = int(battle_list[user.id][0]) - bot_take
    poster = user.poster
    if battle_list[user.id][0] > 0:
        caption = Text.bot_turn(bot_take)
        keyboard = kb_end_game(True)
    else:
        caption = Text.bot_win(bot_take)
        keyboard = kb_end_game()
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id, reply_markup=keyboard)
    await asyncio.sleep(3)
    if battle_list[user.id][0] > 0:
        await player_turn(call, user)


@dp.callback_query_handler(take.filter(button='player'))
async def player_turn(_, user: User):
    if user.data[-1] == 'new_game':
        count = battle_list[user.id][1] // 2
    else:
        _, _, count = user.data
    poster = user.poster
    if battle_list[user.id][0] > 0:
        caption = Text.player_turn(battle_list[user.id][0], count)
        keyboard = kb_take('player', count, user)
    else:
        caption = Text.player_win(count)
        keyboard = kb_end_game()
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id, reply_markup=keyboard)


@dp.callback_query_handler(take.filter(button='take'))
async def player_confirm(call: CallbackQuery, user: User):
    _, _, count = user.data
    battle_list[user.id][0] = int(battle_list[user.id][0]) - int(count)
    poster = user.poster
    if battle_list[user.id][0] > 0:
        caption = Text.player_turn(battle_list[user.id][0], count)
        keyboard = kb_take('player', count, user)
    else:
        caption = Text.player_win(count)
        keyboard = kb_end_game()
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id, reply_markup=keyboard)
    await asyncio.sleep(3)
    if battle_list[user.id][0] > 0:
        await bot_turn(call, user)


@dp.callback_query_handler(mmenu.filter(button='new_game'))
async def new_game(call: CallbackQuery, user: User):
    battle_list[user.id] = [user.max_count, user.turn]
    poster = user.poster
    for i in range(30):
        caption = Text.waiting(i)
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                     chat_id=user.chat_id, message_id=user.message_id)
    draw = random.randint(0, 1)
    caption += (f' {user.name}' if draw else ' Бот!')
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=user.chat_id, message_id=user.message_id)
    if draw == 1:
        await player_turn(call, user)
    else:
        await bot_turn(call, user)
