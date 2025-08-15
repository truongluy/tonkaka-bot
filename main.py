
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Xin chào! Đây là TON Mini Bot. Gõ /help để xem lệnh.")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Các lệnh có sẵn:\n/start - bắt đầu\n/help - trợ giúp\n/create - tạo token (chưa code)\n/game - chơi game (chưa code)\n/referral - xem ref (chưa code)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
