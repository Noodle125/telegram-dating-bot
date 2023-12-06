from telegram import ReplyKeyboardMarkup

def send_message(update, text):
    keyboard = ReplyKeyboardMarkup([['/register', '/search'], ['/profile', '/help']])
    update.message.reply_text(text, reply_markup=keyboard)
