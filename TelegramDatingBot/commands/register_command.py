from telegram import Update, Context
from telegram.ext import CommandHandler

def register_command(update: Update, context: Context):
    update.message.reply_text("Welcome to the Telegram Dating Bot!\n\nUse the following commands to interact with the bot:\n\n/register - Create your profile\n/search - Search for potential matches\n/profile - View your profile\n/help - Get additional help")
