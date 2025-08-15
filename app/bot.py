
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from .config import settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

async def register_builtin_handlers():
    # simple health handler to confirm process is alive
    @dp.message(Command('health'))
    async def health(message: Message):
        await message.reply('OK')

    # other handlers are registered by importing their modules (see main.py)
    logger.info("Builtin handlers registered.")

async def run_bot():
    logger.info("Starting bot...")
    # import handlers here so they register to dp
    from .handlers import start, create, referral  # noqa: E402,F401
    await register_builtin_handlers()
    await dp.start_polling(bot)
