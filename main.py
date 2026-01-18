import asyncio
import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
AMAZON_AFILIADO = os.getenv("AMAZON_AFILIADO")

bot = Bot(token=BOT_TOKEN)

async def postar():
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=(
            "🔥 OFERTA AMAZON 🔥\n\n"
            "📦 Produto em promoção\n"
            "💰 Preço especial\n\n"
            f"👉 https://www.amazon.com.br/?tag={AMAZON_AFILIADO}"
        )
    )

async def loop():
    while True:
        try:
            await postar()
            await asyncio.sleep(3600)  # 1 hora
        except Exception as e:
            print("Erro:", e)
            await asyncio.sleep(60)

asyncio.run(loop())

