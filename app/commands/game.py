
from aiogram.types import Message
from aiogram import Router

router = Router()

@router.message(commands=["game"])
async def game_cmd(message: Message):
    await message.answer("🎮 Mini game demo: tính năng sẽ được cập nhật thêm!")
