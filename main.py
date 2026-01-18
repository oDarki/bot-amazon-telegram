import os
from telegram import Bot
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

async def teste():
    updates = await bot.get_updates()
    print(updates)

asyncio.run(teste())
