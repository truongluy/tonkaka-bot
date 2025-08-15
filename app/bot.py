
import logging
from aiogram import Bot, Dispatcher
from .config import settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
