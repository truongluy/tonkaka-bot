
from aiogram.types import Message
from aiogram import Router
from app.services.referral_utils import generate_ref_link

router = Router()

@router.message(commands=["referral"])
async def referral_cmd(message: Message):
    link = generate_ref_link(message.from_user.id)
    await message.answer(f"🔗 Link giới thiệu của bạn:\n{link}")
