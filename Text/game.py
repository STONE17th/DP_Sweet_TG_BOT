def waiting(count: int):
    return f'Решаем, кто будет ходить первым{"." * (count % 5)}'


def bot_turn(bot_take: int):
    return f'Бот взял {bot_take} конфет'


def bot_win(bot_take: int):
    return f'Бот берет {bot_take} конфет и ПОБЕЖДАЕТ!'


def player_turn(count: int, player_take: int):
    return f'На столе лежит всего {count} конфет...\nCколько возмешь ты? {player_take}?'


def player_after_take(name: str, count: int, take: int):
    return f'{name} взял {take} конфет и на столе осталось {count}...'


def player_win(player_take: int):
    return f'Ты забираешь последние {player_take} конфет и ПОБЕЖДАЕШЬ!'
