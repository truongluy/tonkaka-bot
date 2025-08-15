
from aiogram import Router
from aiogram.types import Message

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

@router.message(commands=['start'])
async def cmd_start(message: Message):
    await message.answer(WELCOME, parse_mode='Markdown')

@router.message(commands=['help'])
async def cmd_help(message: Message):
    await message.answer('Các lệnh hiện có:\n/start\n/help\n/create\n/referral\n/health')
