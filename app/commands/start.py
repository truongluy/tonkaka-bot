
from aiogram.types import Message
from aiogram import Router

router = Router()

WELCOME = (
    "Xin chào! Đây là *TON Mini Bot* 🚀\n"
    "• /help — xem lệnh\n"
    "• /create — tạo token (demo)\n"
    "• /referral — liên kết giới thiệu\n"
    "• /game — mini game"
)

@router.message(commands=["start"])
async def start_cmd(message: Message):
    await message.answer(WELCOME, parse_mode="Markdown")

@router.message(commands=["help"])
async def help_cmd(message: Message):
    await message.answer("Các lệnh có sẵn:\n/start\n/help\n/create\n/referral\n/game")
