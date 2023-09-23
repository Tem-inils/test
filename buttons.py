import telebot.types
from telebot import types

def type1():
    btn_obl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Таблицы')
    # btn2 = types.KeyboardButton('')
    btn_obl.add(btn1)
    return btn_obl

def type2():
    telebot.types.ReplyKeyboardMarkup(selective=False)
    btn_obl = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Времена в Английском', callback_data='time_english')
    btn_obl.add(btn1)
    return btn_obl