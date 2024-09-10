"""
Telegram bot instance
"""

import os
import logging

import telebot

from dumb_telegram_bot.data import LocalPandasDatabase
from dumb_telegram_bot.chains import UserRetrieverRagChain, MimickingChatBot

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()



def create_bot_routes(telegram_json_history: str, n_samples: int = 500):
    
    bot = telebot.TeleBot(os.environ["TELEGRAM_API_TOKEN"])
    
    DATABASE = LocalPandasDatabase(path=telegram_json_history)
    TELEGRAM_USER_LIST = DATABASE.get_unique_users()

    RETRIEVER = UserRetrieverRagChain(list_users=TELEGRAM_USER_LIST)
    CHATBOT = MimickingChatBot()

    @bot.message_handler(commands=["imite", "mimic"])
    def mimic(message):
        """
        Syntax: /imite <user> <theme>
        
        :param message: User message
        :return: None
        """
        
        LOGGER.debug(message.text)

        message.text.split(' ')
        print(message.text)
        split_message = message.text.split(' ')

        if len(split_message)<2:
            bot.reply_to(message, "Incorrect syntax.\nHelp: /imite <user> <theme>")
            return

        user = split_message[1]
        theme = split_message[2:]

        print(f"Queried user: {user}, theme: {theme}")
        telegram_username = RETRIEVER.get_telegram_username(user=user)
        print(f"Found username: {telegram_username}")
        text_samples = DATABASE.get_sample_from_user(n_samples=n_samples, username=telegram_username)
        
        answer = CHATBOT.get_message(text_samples=text_samples, person_to_mimic=telegram_username, theme=theme)

        bot.reply_to(message=message, text=answer)

    return bot