from aiogram import types
from bot import bot


def web_app_keyboard():
    keybord = types.ReplyKeyboardMarkup(row_width=1)
    webApp = types.web