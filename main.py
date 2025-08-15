import os
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"{os.getenv('RENDER_EXTERNAL_URL')}{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
dp = Dispatcher()

app = Flask(__name__)

# --------- Handlers ----------
@dp.message()
async def handle_message(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}, đây là bot webhook trên Render!")

# --------- Webhook Endpoint ----------
@app.route(WEBHOOK_PATH, methods=["POST"])
async def webhook():
    update = Update.model_validate(request.json, context={"bot": bot})
    await dp.feed_update(bot, update)
    return "OK"

# --------- Setup Webhook ----------
@app.before_first_request
def setup_webhook():
    asyncio.get_event_loop().run_until_complete(bot.set_webhook(WEBHOOK_URL))
    print(f"Webhook set: {WEBHOOK_URL}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
