import json
from states.class_User import User
import datetime
from loader import bot
from telebot.types import  CallbackQuery

def recording_history_in_json(id) -> None:
    """Которая открывает базу данных(JSON),
    проверяет есть ли в базе ID юзера,
    если нет то добавляет в базу,
     если есть то дописывает его историю поиска
     :param id: int
     :return: None"""
    user = User.get_user(id)
    # TODO в данном месте она не используется вы ее объявляете ниже
    work_data = {}
    with open('data_json.json', 'r') as file:
        work_data = json.load(file)
        print(work_data)
    if str(id) in work_data.keys():
        date_time = datetime.datetime.now()
        key_data_time = date_time.strftime('%d-%m-%Y %H:%M:%S')
        work_data[str(id)].append({key_data_time: {'mode': user.mode,
                                              'hotel': [hotel['name'] for hotel in user.total_data_hotel]}})

        with open('data_json.json', 'w') as file:
            json.dump(work_data, file, indent=4)
    else:
        work_data[id] = [{str(datetime.datetime.now()): {'mode': user.mode,
                                                'hotel': [hotel['name'] for hotel in user.total_data_hotel]}}]
        # TODO этот кусок кода явно повторяется его можно вынести в функцию
        with open('data_json.json', 'w') as file:
            json.dump(work_data, file, indent=4)


def output_history_in_json(call: CallbackQuery) -> None:
    """Функция для чтения и поиска истории из базы данных,
     а так же для вывода информации юзеру.
     :param call: CallbackQuery
     :return: None"""
    # TODO код сломается у меня он не запуститься
    # TODO пути должны быть относительные + \\ заменить на / или использовать метод который сам подставит нужные
    with open('C:\\Users\\Wolfich\\PycharmProjects\\Diplom_telegram_bot\\data_json.json', 'r') as file:
        data_history = json.load(file)
    if str(call.from_user.id) in data_history:

        for keys, value in enumerate(data_history[str(call.from_user.id)]):
            bot.send_message(call.from_user.id, f'Дата и время: {[index for index in value.keys()][0]}\n'
                                                f'Режим поиска: {[index for index in value.values()][0]["mode"]}\n'
                                                f'Найденные отели: {[index for index in value.values()][0]["hotel"]}')
    else:
        bot.send_message(call.from_user.id, 'Извините, но вы ничего не искали.')