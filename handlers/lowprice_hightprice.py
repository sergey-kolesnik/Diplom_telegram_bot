from loader import bot
from loguru import logger
from states.class_User import User
from keyboards.inline import menu
from telebot.types import CallbackQuery, Message
import re
from handlers import bestdeal


def sorting_lowprice_hightprice(id: int) -> list[dict]:
    """Функция, которая сортирует отели по критерию "самые дешевые"
     или самые дорогие, в зависимости от выбранного режима
     :param id: int
     :return hotel: list[dict]"""
    user = User.get_user(id)
    data = user.total_data_hotel
    count = user.hotels_count
    pattern = (r'[$|€]')
    for price in data:
        price['price'] = int(re.sub(pattern, '', price['price']))
    if user.mode == 'топ дешевых отелей':
        hotels = sorted(data, key=lambda k: k['price'])
        if len(hotels) > count:
            hotels = hotels[:count]
            logger.info(hotels)
        return hotels

    elif user.mode == 'топ дорогих отелей':
        hotels = sorted(data, key=lambda k: k['price'], reverse=True)
        if len(hotels) > count:
            hotels = hotels[:count]
            logger.info(hotels)

        return hotels


@logger.catch()
def count_city(call: CallbackQuery) -> None:
    """Функция для запроса у пользователя, какое количество отелей найти
    :param call: CallbackQuery
    :return: None"""
    bot.send_message(call.message.chat.id, 'Отлично, а теперь введите количество отелей которое нужно вывести на экран\n'
                                      'от 1 до 15:')
    logger.info(call.message.chat.id)
    bot.register_next_step_handler(call.message, check_count_city)


@logger.catch()
def check_count_city(message: Message) -> None:
    """Функция проверки правильности введеного числа
    :param message: Message
    :return: None"""
    logger.info(message.text)

    try:
        count = int(message.text)
        if 0 < count <= 15:
            user = User.get_user(message.from_user.id)
            user.hotels_count = count
            logger.info(user.hotels_count)

        else:
            raise ValueError('Не корректное значение')
    except ValueError:
        bot.send_message(message.from_user.id, 'Будьте добры, цифрами\n'
                                               'от 1 до 15:')
        bot.register_next_step_handler(message, check_count_city)
    else:
        if user.mode == 'по цене и расположению от центра':
            bestdeal.bestdeal(message)
        else:
            user.total_data_hotel = sorting_lowprice_hightprice(message.from_user.id)
            logger.info(user.total_data_hotel)
            menu.keyboard_photo(message.from_user.id)
