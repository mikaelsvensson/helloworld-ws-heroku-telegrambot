import os

from flask import Flask
from twx.botapi import TelegramBot

application = Flask(__name__)

bot_api_key = os.environ.get('TELEGRAM_BOT_APIKEY')

bot = TelegramBot(bot_api_key)

from app import views
