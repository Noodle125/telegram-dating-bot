from telegram import Update, Context
from telegram.ext import CommandHandler

def help_command(update: Update, context: Context):
    update.message.reply_text("Help!")
