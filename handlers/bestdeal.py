from loader import bot
import re
from loguru import logger
from states.class_User import User
from keyboards.inline import menu
from telebot.types import Message


def bestdeal(message: Message) -> None:
    """Функция которая просит юзера ввести диапазон цен
    :param message: Message
    :return: None"""
    logger.info(message)
    bot.send_message(message.chat.id, 'Введите диапазон цен\nпример(0 100\ 0 - 100):')
    bot.register_next_step_handler(message, checks_the_price_range)




def checks_the_price_range(message: Message) -> None:
    """Функция проверяет правильности ввода диапазона цен
    :param message: Message
    :return None"""
    logger.info(message.text)
    try:
        result_price_range = re.split(r' +', message.text)
        logger.info(result_price_range)
        for check in result_price_range:
            if not check.isdigit():
                result_price_range.remove(check)
        if len(result_price_range) != 2:
            logger.info(result_price_range)

            raise Exception
        logger.info(result_price_range)

    except Exception:
        bot.send_message(message.chat.id, 'Введите диапазон цен правильно\n'
                                          'пример(0 100\ 0 - 100):')
        bot.register_next_step_handler(message, checks_the_price_range)
    else:
        user = User.get_user(message.chat.id)
        result_price_range = [int(index) for index in result_price_range]
        user.price_range = sorted(result_price_range)
        logger.info(user.price_range)
        bot.send_message(message.chat.id, 'Введите диапазон расстояния от центра в метрах\n'
                                          'пример(0 100\ 0 - 100):')
        bot.register_next_step_handler(message, checks_the_distance_range)



@logger.catch()
def checks_the_distance_range(message: Message) -> None:
    """Функция проверяет правильности ввода диапазона расстояния
    :param message: Message
    :return None"""
    try:
        result_distance_range = re.split(r' +', message.text)
        logger.info(result_distance_range)
        for check in result_distance_range:
            if not check.isdigit():
                result_distance_range.remove(check)
        if len(result_distance_range) != 2:
            logger.info(result_distance_range)

            raise Exception
        logger.info(result_distance_range)

    except Exception:
        bot.send_message(message.chat.id, 'Введите диапазон расстояния от центра правильно в метрах\n'
                                          'пример(0 100\ 0 - 100):')
        bot.register_next_step_handler(message, checks_the_price_range)
    else:
        user = User.get_user(message.chat.id)
        result_distance_range = [int(index) for index in result_distance_range]
        user.distance_range = sorted(result_distance_range)
        logger.info(user.distance_range)

        user.total_data_hotel = sorting_bestdeal(message)
        try:
            if not user.total_data_hotel:
                raise Exception
        except Exception:
            bot.send_message(message.chat.id, 'В вашем диапазоне ничего не найдено, попробуйте еще раз')
            bot.register_next_step_handler(message, bestdeal)
        else:
            menu.keyboard_photo(message.from_user.id)


def sorting_bestdeal(message: Message) -> list[dict]:
    """Функция сортировки результата по критериям выбранного диапазона цен и расстояния,
    сначала сортируется по ценам, затем по расстоянию, от дешевых до дорогих
    :param message: Message
    :return: list[dict]"""
    user = User.get_user(message.chat.id)
    data = user.total_data_hotel
    pattern = (r'[$|€]')
    for price in data:
        price['price'] = int(re.sub(pattern, '', price['price']))

    pattern = (r'[a-zA-Z]')
    for distance in data:
        distance['distance'] = float(re.sub(pattern, '', distance['distance'])) * 1609

    logger.info(data)
    hotels = [index for index in data if user.price_range[0] <= index['price'] <= user.price_range[1]]
    result_hotels = [index for index in hotels if user.distance_range[0] <= index['distance'] <= user.distance_range[1]]
    hotels = sorted(result_hotels, key=lambda k: k['price'])
    logger.info(hotels)

    if len(hotels) > user.hotels_count:
        hotels = hotels[:user.hotels_count]
        logger.info(hotels)
    return hotels






