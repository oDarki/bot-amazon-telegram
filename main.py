import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

async def main():
    while True:
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text="🤖 Bot Amazon está online e funcionando!"
            )
            await asyncio.sleep(3600)  # 1 hora
        except Exception as e:
            print("Erro:", e)
            await asyncio.sleep(10)

asyncio.run(main())
