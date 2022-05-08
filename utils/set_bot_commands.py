from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_default_commands(bot):
    # TODO дописать докстринги всем методам\функциям
    bot.set_my_commands(
        # TODO однобуквенные переменные заменить на развернутые
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
