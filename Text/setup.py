def main(max_: int, turn: int) -> str:
    return f'Сейчас максимальное количество конфет {max_},\n' \
           f'а за один раз можно взять не более {turn} конфет\n' \
           f'Что будем менять?'


def count(cnt: int) -> str:
    return f'Установим максимальное количество конфет - {cnt}'


def turn(trn: int) -> str:
    return f'За ход можно взять от 1 до {trn} конфет'
