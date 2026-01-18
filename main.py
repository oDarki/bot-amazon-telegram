import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
AFILIADO = os.getenv("AFILIADO")

async def receber_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if "amazon." not in texto:
        await update.message.reply_text("❌ Manda um link da Amazon.")
        return

    if "tag=" not in texto:
        if "?" in texto:
            link = texto + f"&tag={AFILIADO}"
        else:
            link = texto + f"?tag={AFILIADO}"
    else:
        link = texto

    mensagem = f"""🔥 OFERTA AMAZON 🔥

👉 {link}

🛒 Aproveite antes que acabe!
"""

    await context.bot.send_message(chat_id=CHANNEL_ID, text=mensagem)
    await update.message.reply_text("✅ Postado no canal!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_link))

app.run_polling()

