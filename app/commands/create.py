
from aiogram.types import Message
from aiogram import Router
from app.services.ton_utils import create_ton_token_demo

router = Router()

@router.message(commands=["create"])
async def create_cmd(message: Message):
    # Demo: chưa kết nối SDK thật, chỉ mô phỏng để test UI
    token = create_ton_token_demo(name="DemoToken", symbol="DEMO")
    await message.answer(
        "🧪 Tạo token demo thành công!\n"
        f"• Name: {token['name']}\n"
        f"• Symbol: {token['symbol']}\n"
        f"• Address: `{token['address']}`\n"
        f"• Explorer: {token['explorer']}",
        parse_mode="Markdown"
    )
