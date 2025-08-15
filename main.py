import os
import asyncio
import threading
from flask import Flask
from app.bot import run_bot

# Tạo Flask app để Render thấy port
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))  # Render sẽ set biến PORT
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Chạy Flask server trên thread riêng
    threading.Thread(target=run_flask).start()

    # Chạy bot Telegram
    asyncio.run(run_bot())
