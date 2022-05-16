from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_default_commands(bot):
    """Функция для генерации команд бота
    :param bot: telebot
    :return: None"""
    bot.set_my_commands(
        [BotCommand(* check) for check in DEFAULT_COMMANDS]
    )
