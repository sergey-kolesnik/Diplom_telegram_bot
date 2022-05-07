from telebot.types import Message
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    """Эхо хендлер, куда летят текстовые сообщения без указанного состояния
    :param message: Message
    :return: None"""
    bot.reply_to(message, "Эхо без состояния или фильтра.\nСообщение:"
                          f"{message.text}"
                          f"Нажмите /start или /help")
