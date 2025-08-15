
import asyncio
import logging
from app.bot import bot, dp
from app.commands import start, create, referral, game

async def main():
    logging.getLogger(__name__).info("Starting TON Mini Bot...")
    dp.include_router(start.router)
    dp.include_router(create.router)
    dp.include_router(referral.router)
    dp.include_router(game.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
