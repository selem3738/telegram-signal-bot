from telegram import Bot
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if __name__ == "__main__":
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text="🚀 ربات با موفقیت اجرا شد!")
