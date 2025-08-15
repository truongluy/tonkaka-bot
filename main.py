
import asyncio
import logging
from app.bot import run_bot

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        pass
