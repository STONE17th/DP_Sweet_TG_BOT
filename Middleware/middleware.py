from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from Classes import User
from loader import db


class AddSuperData(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        db.new_user(message.from_user.id)
        poster = db.poster(message.from_user.id)
        settings = db.me(message.from_user.id)
        data['user'] = User(message, poster, settings)

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        db.new_user(call.from_user.id)
        poster = db.poster(call.from_user.id)
        settings = db.me(call.from_user.id)
        data['user'] = User(call, poster, settings)
