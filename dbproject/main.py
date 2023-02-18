import telegram
import Constants as keys
from telegram.ext import *
import Responses as R
import logging

bot = telegram.Bot(token=keys.API_KEY)


logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s', level=logging.INFO)

print("Bot started...")


def start_command(update, context):
    update.message.reply_text("Hello it is questions bot!\nEnd your question with '?' ")


def help_command(update, context):
    update.message.reply_text("""
    /start - Start Bot
/help - A list of available commands
/q - Get a true response of smth, that bothering you
/meme - Get one of DDLopata favorite memes
/p - Get a probability of smth
Please end your question with '?' to receive an answer
""")

def question_command(update, context):
    text = str(update.message.text).lower()
    response = R.responses(text)
    update.message.reply_text(response)

def meme_command(update, context):
    response = R.chooseRandomImage()
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(response, 'rb'))



def percent_command(update, context):
    text = str(update.message.text).lower()
    response = R.responseByProcent(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp: object = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("q", question_command))
    dp.add_handler(CommandHandler("meme", meme_command))
    dp.add_handler(CommandHandler("p", percent_command))


    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idle()


main()
