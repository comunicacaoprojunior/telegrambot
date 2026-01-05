import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_BASE_URL = os.getenv("WEBHOOK_BASE_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "webhook")
PORT = int(os.getenv("PORT", "10000"))

COMMANDS = {
    "regras": [
        "📌 Regras do grupo",
        "1) Seja respeitoso",
        "2) Sem spam",
        "3) Use os comandos do bot",
    ],
    "umbrella": [
        "BECAAAAAAUSE",
        "WHEN THE SUN SHINE WE SHINE TOGETHER",
        "YOU CAN STAND UNDER MY UMBRELLA ELLA ELLA ☂️☂️☂️",
        "💧☂️ Ê Ê Ê ☂️💧",
    ],
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Eai, MC Carlinhos 2.0 na área!! Bom e novo, 100% atualizado!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    webhook_url = f"{WEBHOOK_BASE_URL}/{WEBHOOK_SECRET}"

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=WEBHOOK_SECRET,
        webhook_url=webhook_url
    )

if __name__ == "__main__":
    main()

