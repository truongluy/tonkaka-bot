
from aiogram import Router
from aiogram.types import Message
from app.services.ton import create_ton_token_demo
from aiogram.filters import Command

router = Router()

@router.message(Command("create"))
async def cmd_create(message: Message):
    # Demo implementation: returns a mocked token object (safe to run on Render/testnet)
    token = create_ton_token_demo(name='DemoToken', symbol='DEMO')
    text = (
        f'🧪 Token demo đã tạo!\n'
        f'• Name: {token["name"]}\n'
        f'• Symbol: {token["symbol"]}\n'
        f'• Address: `{token["address"]}`\n'
        f'• Explorer: {token["explorer"]}'
    )
    await message.answer(text, parse_mode='Markdown') 
