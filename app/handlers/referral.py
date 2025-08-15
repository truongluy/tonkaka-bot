
from aiogram import Router
from aiogram.types import Message
from app.services.referral import generate_ref_link

router = Router()

@router.message(commands=['referral'])
async def cmd_referral(message: Message):
    link = generate_ref_link(message.from_user.id)
    await message.answer(f'🔗 Link giới thiệu của bạn:\n{link}')
