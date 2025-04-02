import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я Ozzy X — твой помощник по Ozon.")

def report(update, context):
    context.bot.send_message(chat_id=CHANNEL_ID, text="📊 Ежедневный отчёт: (здесь будет аналитика)")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("report", report))

updater.start_polling()

fix: changed command to latin
