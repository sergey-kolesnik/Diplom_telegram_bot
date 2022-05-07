from loader import bot
from loguru import logger
from handlers.default_heandlers import start
from utils.set_bot_commands import set_default_commands


logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='1000 KB')

try:
    @logger.catch()
    def main():
        if __name__ == '__main__':
            set_default_commands(bot)
            bot.infinity_polling()
    main()
except Exception as error:
    pass



