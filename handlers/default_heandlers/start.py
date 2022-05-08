from telebot.types import Message, CallbackQuery
from states.class_User import User
from loader import bot
from loguru import logger
from keyboards.inline.menu import keyboard_menu
from utils.search_for_hotels import city
from utils.properties_list import properties
from handlers import lowprice_hightprice
from requests import get
from database.database import recording_history_in_json, output_history_in_json


@bot.message_handler(commands=['start'])
@logger.catch()
def bot_start(message: Message) -> None:
    """Функция приветсвия пользователя, которая создает экземпляр класса
    :param message: Message
    :return: None"""
    text = f'Привет {message.from_user.full_name}, меня зовут Спутник, я помогу подобрать тебе отель!'
    # TODO лишние скобки, почему не открыли через контекстный менеджер
    photo1 = open(('sputnik.jpg').encode('utf-8'), 'rb')
    bot.send_photo(message.from_user.id, caption=text, photo=photo1)
    User.get_user(message.from_user.id)

    logger.info(message.chat.id)
    logger.info(message)

    user = User.get_user(message.from_user.id)
    user.user_name = message.from_user.full_name
    user.chat_id = message.chat.id

    logger.info(User.get_user(message.from_user.id))
    logger.info(User.data_user_in_class)
    logger.info(message)

    keyboard_menu(message.from_user.id)


def next_city(call: CallbackQuery) -> None:
    """Функция, которая запрашивает у пользователя город в котором искать отель
    :param call: CallbackQuery
    :return: None"""
    bot.send_message(call.message.chat.id, 'Отлично, а теперь введите город в котором хотите найти отель:')
    bot.register_next_step_handler(call.message, registration_city)


@logger.catch()
def registration_city(message: Message) -> None:
    """Функция которая присваивает атрибут city_user классу User
    :param message: Message
    :return: None"""
    city_user = message.text
    user = User.get_user(message.from_user.id)
    user.city_user = city_user
    logger.info(message)
    city(message)


@logger.catch()
def output_of_the_result(message: Message):
    """Функция для вывода конечного результата юзеру, а также запускает функцию
    recording_history_in_json() для записи истории поиска
    :param message: Message
    :return: None"""
    user = User.get_user(message.chat.id)
    logger.info(message.chat.id)
    logger.info(user.total_data_hotel)
    bot.send_message(message.chat.id, 'Отлично, начинаю поиск ◴◴◴▁ ▂ ▃ ▄ ▅ ▆ ▇ █')

    if user.photo == 'yes':
        for hotel in user.total_data_hotel:
            url = get(hotel["photo"])
            bot.send_photo(message.chat.id, caption=None, photo=url.content)
            bot.send_message(message.chat.id, f'Название отлеля: {hotel["name"]}\n '
                                              f'Регион: {hotel["countryName"]}\n '
                                              f'Адрес: {hotel["streetaddress"]}\n '
                                              f'Расстояние от центра: {hotel["distance"]}\n'
                                              f'Количество звезд: {hotel["star"]}\n'
                                              f'Цена: {hotel["price"]}$\n '
                                              f'Ссылка: {hotel["url"]}')
    elif user.photo == 'no':
        for hotel in user.total_data_hotel:
            bot.send_message(message.chat.id, f'Название отлеля: {hotel["name"]}\n '
                                              f'Регион: {hotel["countryName"]}\n '
                                              f'Адрес: {hotel["streetaddress"]}\n '
                                              f'Расстояние от центра: {hotel["distance"]}'
                                              f'Количество звезд: {hotel["star"]}\n'
                                              f'Цена: {hotel["price"]}$\n '
                                              f'Ссылка: {hotel["url"]}')
    recording_history_in_json(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
@logger.catch()
def callback_menu(call: CallbackQuery) -> None:
    """Функция-обработчик клавиатуры.
    :param call: CallbackQuery
    :return: None"""
    user = User.get_user(call.from_user.id)
    logger.info(call.data)
    logger.info(call.message)
    logger.info(call)
    if call.data == 'lowprice':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        user.mode = 'топ дешевых отелей'
        next_city(call)

    elif call.data == 'highprice':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        user.mode = 'топ дорогих отелей'
        next_city(call)

    elif call.data == 'bestdeal':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        user.mode = 'по цене и расположению от центра'
        logger.info(user.mode)
        next_city(call)

    elif call.data == 'history':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        logger.info(call)
        output_history_in_json(call)

    elif call.data == 'yes':
        logger.info(call.data)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        user.photo = 'yes'
        output_of_the_result(call.message)

    elif call.data == 'no':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        user.photo = 'no'
        output_of_the_result(call.message)

    elif call.data:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='ok')
        # TODO ожидается не тот тип
        result = properties(call.data)
        user.total_data_hotel = result
        logger.info(user.total_data_hotel)
        logger.info(call)

        lowprice_hightprice.count_city(call)