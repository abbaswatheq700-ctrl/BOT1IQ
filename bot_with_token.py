import time
import telebot

TOKEN = "8221862139:AAGXlO_OpMQ1QEGKOhBMd18-zh3u4u7GZLA"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "هلا بيك 👋\nالبوت اشتغل بنجاح على الاستضافة ✅")

@bot.message_handler(commands=["ping"])
def ping(message):
    bot.reply_to(message, "Pong! 🟢\nالبوت شغال.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text:
        bot.reply_to(message, f"استلمت: {message.text}")

def run():
    print("Starting Telegram bot...")
    while True:
        try:
            print("Polling started.")
            bot.infinity_polling(
                timeout=30,
                long_polling_timeout=30,
                skip_pending=True
            )
        except Exception as e:
            print(f"Bot stopped بسبب خطأ: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    run()
