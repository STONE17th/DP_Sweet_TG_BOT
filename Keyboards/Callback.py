from aiogram.utils.callback_data import CallbackData

mmenu = CallbackData('main', 'button')

setup = CallbackData('setup', 'button', 'count')

take = CallbackData('player', 'button', 'count')

pvp_confirm = CallbackData('pvp', 'confirm', 'button')
