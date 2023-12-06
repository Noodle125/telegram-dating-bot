from telegram import Update, Context
from telegram.ext import CommandHandler

def profile_command(update: Update, context: Context):
    update.message.reply_text("View your profile!")
