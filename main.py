import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

if os.getenv("STARTED") != "1":
    bot.send_message(chat_id=CHANNEL_ID, text="🤖 Bot Amazon está online!")
    os.environ["STARTED"] = "1"
import os
import asyncio
from telegram import Bot
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Amazon rodando"

async def bot_loop():
    while True:
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text="🤖 Bot Amazon está online!"
            )
            await asyncio.sleep(60)
        except Exception as e:
            print("Erro:", e)
            await asyncio.sleep(10)

def start_bot():
    asyncio.run(bot_loop())

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
