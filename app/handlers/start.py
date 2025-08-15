
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

WELCOME = (
    "🚀 *TON Mini Bot*\n\n"
    "Chào mừng! Các lệnh mẫu:\n"
    "• /start — bắt đầu\n"
    "• /help — trợ giúp\n"
    "• /create — tạo token (demo)\n"
    "• /referral — lấy link giới thiệu\n"
    "• /health — kiểm tra bot"
)
@router.message(Command("start", "help"))

async def cmd_start(message: Message):
    await message.answer(WELCOME, parse_mode='Markdown')

async def cmd_help(message: Message):
    await message.answer('Các lệnh hiện có:\n/start\n/help\n/create\n/referral\n/health')
