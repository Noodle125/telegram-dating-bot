from telegram import Updater
from telegram.ext import CommandHandler

from commands import register_command, search_command, profile_command, help_command

updater = Updater('YOUR_TELEGRAM_BOT_TOKEN')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('register', register_command))
