from aiogram.types import Message, CallbackQuery

from loader import db


class User:
    def __init__(self, message: Message | CallbackQuery, poster: tuple[str], settings: tuple):
        self.name = message.from_user.first_name
        self.id = message.from_user.id
        self.max_count = settings[0]
        self.turn = settings[1]
        self.poster = poster[0] if poster[
            0] else 'AgACAgIAAxkBAAICEWRiq-NM5NccUQ_VTkUzHEjR4XwgAALSzTEbDjYYS0mlb_0EunV8AQADAgADcwADLwQ'
        if isinstance(message, Message):
            self.chat_id = message.chat.id
            self.message_id = message.message_id
            self.data = message.text
        elif isinstance(message, CallbackQuery):
            self.chat_id = message.message.chat.id
            self.message_id = message.message.message_id
            self.data = message.data.split(':')

    def refresh(self):
        self.max_count, self.turn = db.me(self.id)
