import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_BASE_URL = os.getenv("WEBHOOK_BASE_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "webhook")
PORT = int(os.getenv("PORT", "10000"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Eai, MC Carlinhos 2.0 na área!! Bom e novo, 100% atualizado!")

async def umbrella(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("BECAAAAAAUSE🎤🎤🎤")
    await asyncio.sleep(1)
    await update.message.reply_text("WHEN THE SUN SHINE WE SHINE TOGETHER🌟")
    await asyncio.sleep(1)
    await update.message.reply_text("YOU CAN STAND UNDER MY UMBRELLA ELLA ELLA ☂️☂️☂️")
    await asyncio.sleep(1)
    await update.message.reply_text("💧☂️ Ê Ê Ê ☂️💧")
    await asyncio.sleep(1)
    await update.message.reply_photo(
        photo="https://raw.githubusercontent.com/comunicacaoprojunior/telegrambot/refs/heads/main/assets/rihanna.jpg")

async def caveirao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("caveirão...")
    await asyncio.sleep(1)
    await update.message.reply_text("...")
    await asyncio.sleep(1)
    await update.message.reply_text("caveirão...")
    await asyncio.sleep(1)
    await update.message.reply_text("cave cave")
    await asyncio.sleep(1)
    await update.message.reply_text("cave caveirão...")
    await asyncio.sleep(1)
    await update.message.reply_text("caveirão...")
    await asyncio.sleep(1)
    await update.message.reply_text("A PRO JUNIOR CHEGOUUUUUU😎🔥")
    await asyncio.sleep(1)
    await update.message.reply_text("A PRO JUNIOR CHEGOUUU🔥🔥🔥 - DJ CARLOS!")
    await asyncio.sleep(1)
    await update.message.reply_animation(
    animation="https://raw.githubusercontent.com/comunicacaoprojunior/telegrambot/main/assets/Caveirao.gif")

async def carute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("carutê...🍷🥀")
    await asyncio.sleep(1)
    await update.message.reply_text("ca ca ca ca ca🗿")
    await asyncio.sleep(1)
    await update.message.reply_text("ca carutê... tê.. tê..🍷")
    await asyncio.sleep(1)
    await update.message.reply_text("carutê🥀")
    await asyncio.sleep(1)
    await update.message.reply_text("...")
    await asyncio.sleep(1)
    await update.message.reply_text("la vida, la vida es un CARUTÊ TÊ TÊ☠️☠️☠️")
    await asyncio.sleep(1)
    await update.message.reply_text("CARUTÊ Ê Ê🗿🥀🍷")
    await asyncio.sleep(1)
    await update.message.reply_photo(
        photo="https://raw.githubusercontent.com/comunicacaoprojunior/telegrambot/refs/heads/main/assets/carute.png")
    await asyncio.sleep(1)
    await update.message.reply_photo(
        photo="https://raw.githubusercontent.com/comunicacaoprojunior/telegrambot/refs/heads/main/assets/aura.jpg")
    
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("umbrella", umbrella))
    app.add_handler(CommandHandler("caveirao", caveirao))
    app.add_handler(CommandHandler("carute", carute))

    webhook_url = f"{WEBHOOK_BASE_URL}/{WEBHOOK_SECRET}"

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=WEBHOOK_SECRET,
        webhook_url=webhook_url
    )

if __name__ == "__main__":
    main()







