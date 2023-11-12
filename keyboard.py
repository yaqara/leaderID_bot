from aiogram import types
from aiogram.types.web_app_info import WebAppInfo


def authKeyboard():
    keybord = types.InlineKeyboardMarkup()
    btns = [
        types.InlineKeyboardButton(text="Нет", callback_data="regPressed"),
        types.InlineKeyboardButton(text="Да", callback_data="loginPressed")
    ]
    keybord.add(*btns)
    return keybord

def webKeyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btns = [
        types.KeyboardButton(text="Web app", web_app=WebAppInfo(url='https://127.0.0.1:8000'))
    ]
    keyboard.add(*btns)
    return keyboard