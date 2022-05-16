import requests
from config_data.config import RAPID_API_KEY
from loguru import logger
import json
from loader import bot
from telebot.types import CallbackQuery


def properties(id_region: CallbackQuery) -> list[dict]:
    """Функция для поиска отелей в конкретно выбранном регионе
    :param id_region: int
    :return: list[dict]"""
    data_hotel = []
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": id_region.data,
                   "pageNumber": "1",
                   "pageSize": "25",
                   "checkIn": "2020-01-08",
                   "checkOut": "2020-01-15",
                   "adults1": "1",
                   "sortOrder": "PRICE",
                   "locale": "en_US",
                   "currency": "USD"}

    headers = {
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
        "X-RapidAPI-Key": RAPID_API_KEY
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=15)
    try:
        if response.status_code == requests.codes.ok:

            suggestions = json.loads(response.text)
            data = suggestions['data']['body']['searchResults']['results']
            for check, index in enumerate(data):
                try:
                    data_hotel.append({'id': index['id'],
                                       'name': index['name'],
                                       'streetaddress': index['address']['streetAddress'],
                                       'countryName': index['address']['countryName'],
                                       'distance': index['landmarks'][0]['distance'],
                                       'price': index['ratePlan']['price']['current'],
                                       'url': 'https://hotels.com/ho' + str(index['id']),
                                       'star': int(index['starRating']),
                                       'photo': index['optimizedThumbUrls']['srpDesktop']})
                except KeyError:
                    logger.error(index)

            logger.info(data_hotel)
            return data_hotel

        else:
            raise ConnectionError('Ошибка подключения')
    except ConnectionError:
        logger.error(response.status_code)
        bot.send_message(id_region.from_user.id, 'Извините, техническая неисправность, мы уже работаем над проблемой')

