from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot
from loguru import logger
from handlers import  bestdeal, lowprice_hightprice
from utils.properties_list import properties
from states.class_User import User


def keyboard_menu(id: int) -> None:
    """Функция клавиатуры основного меню
    id: int
    return: None
    """
    keyboards = InlineKeyboardMarkup(row_width=1)
    lowprice = InlineKeyboardButton(text='топ самых дешёвых отелей в городе', callback_data='lowprice')
    highprice = InlineKeyboardButton(text='топ самых дорогих отелей в городе', callback_data='highprice')
    bestdeal = InlineKeyboardButton(text='наиболее подходящих по цене и расположению от центра',
                                    callback_data='bestdeal')
    history = InlineKeyboardButton(text='узнать историю поиска', callback_data='history')
    keyboards.add(lowprice,
                  highprice,
                  bestdeal,
                  history)
    bot.send_message(id, text='Выбери категорию:', reply_markup=keyboards)


def keyboard_photo(id: int) -> None:
    """Функция, конструкция клавиатуры из 2 кнопок, для загрузки фото отелей
    :param id: int
    :return: None"""
    keyboards = InlineKeyboardMarkup()
    key_yes = InlineKeyboardButton('Да', callback_data='yes')
    key_no = InlineKeyboardButton('Нет', callback_data='no')
    keyboards.add(key_yes, key_no)
    bot.send_message(id, text='Хотите загрузить фото?', reply_markup=keyboards)




