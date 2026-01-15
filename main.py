import os
import requests
import random
from telegram import Bot
from telegram.constants import ParseMode
from time import sleep

BOT_TOKEN = os.getenv("BOT_TOKEN")
AMAZON_TAG = os.getenv("AMAZON_TAG")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # ex: @seucanal

bot = Bot(token=BOT_TOKEN)

# ==========================
# SIMULAÇÃO DE PRODUTOS
# (depois trocamos por API oficial)
# ==========================
PRODUCTS = [
    {
        "title": "Echo Dot 5ª Geração",
        "old_price": 499.90,
        "new_price": 299.90,
        "image": "https://m.media-amazon.com/images/I/61EXU8BuGZL._AC_SL1000_.jpg",
        "link": "https://www.amazon.com.br/dp/B09B8V1LZ3"
    },
    {
        "title": "Fire TV Stick Lite",
        "old_price": 349.90,
        "new_price": 219.90,
        "image": "https://m.media-amazon.com/images/I/51CgKGfMelL._AC_SL1000_.jpg",
        "link": "https://www.amazon.com.br/dp/B091G4YP57"
    }
]

def post_product():
    product = random.choice(PRODUCTS)

    discount = int(
        100 - (product["new_price"] / product["old_price"] * 100)
    )

    affiliate_link = f'{product["link"]}?tag={AMAZON_TAG}'

    caption = f"""
🟠 <b>AMAZON — OFERTA</b>

🔥 <b>{product["title"]}</b>

💸 De <s>R$ {product["old_price"]:.2f}</s>
👉 <b>Por R$ {product["new_price"]:.2f}</b>
📉 <b>{discount}% OFF</b>

🔗 <a href="{affiliate_link}">Comprar agora</a>
"""

   await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=product["image"],
        caption=caption,
        parse_mode=ParseMode.HTML
    )

# ==========================
# LOOP AUTOMÁTICO
# ==========================
if __name__ == "__main__":
    while True:
        try:
            post_product()
            sleep(3600)  # 1 post por hora
        except Exception as e:
            print("Erro:", e)
            sleep(60)
