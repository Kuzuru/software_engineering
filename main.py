import logging
import os

from src.bot import Bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

_TOKEN = "CURRENCY_OUTLOOK_BOT_TOKEN"


def main(bot_token):
    bot = Bot(bot_token)
    bot.run_polling()


if __name__ == "__main__":
    BOT_TOKEN = os.environ.get(_TOKEN)
    if BOT_TOKEN:
        main(BOT_TOKEN)
    else:
        logger.error("Couldn't obtain bot token from system environment")
