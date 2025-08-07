import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Увімкнення логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Головне меню
main_menu = [['Додати дані'], ['Показати останні 7 записів']]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Привіт! Це бот для збору тиску, пульсу та коментарів.\n\nВибери опцію нижче:',
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(f'Ви обрали: {text} (але ця функція ще не реалізована)')

def main():
    # Токен тимчасово порожній – ми вставимо його пізніше
    updater = Updater("8300226247:AAHbIQimX7krzDJu5UMHLXKpXSi9Ueez2as", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
