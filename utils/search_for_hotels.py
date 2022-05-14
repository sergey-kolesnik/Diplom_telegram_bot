import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from loader import bot
from config_data.config import RAPID_API_KEY
import json
import re
from loguru import logger


@logger.catch()
def city(message: Message) -> None:
    """Функция поиска отелей в городе
    :param message: Message
    :return: None"""
    cities = list()
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {'query': message.text, 'locale': 'en_US', 'currency': 'USD'}

    headers = {
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
        "X-RapidAPI-Key": RAPID_API_KEY
    }

    # TODO при любом гет запросе должен быть аргумент timeout и мы его должны отлавливать и логировать
    response = requests.get(url, headers=headers, params=querystring, timeout=15)
    pattern = r'(?<="CITY_GROUP",).+?[\]]'
    find = re.search(pattern, response.text)
    if find:
        suggestions = json.loads(f"{{{find[0]}}}")
        clear = r'<.*?>|</.*?>'
        for dest_id in suggestions['entities']:
            clear_destination = re.sub(clear, '', dest_id['caption'])
            cities.append({'city_name': clear_destination, 'destination_id': dest_id['destinationId']})
    destinations = InlineKeyboardMarkup(row_width=1)

    for town in cities:
        destinations.add(InlineKeyboardButton(text=town['city_name'],
                                              callback_data=int(f'{town["destination_id"]}')))

    bot.send_message(message.from_user.id, 'Уточните, пожалуйста:', reply_markup=destinations)
