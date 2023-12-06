from telegram import Update, Context
from telegram.ext import CommandHandler

def search_command(update: Update, context: Context):
    update.message.reply_text("Search for matches!")
