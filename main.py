import logging
import os
from dotenv import load_dotenv, dotenv_values
from src.bot import Bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()  # take environment variables from .env.
_TOKEN_KEY = "CURRENCY_OUTLOOK_BOT_TOKEN"


def main(bot_token):
    bot = Bot(bot_token)
    bot.run_polling()


if __name__ == "__main__":
    BOT_TOKEN = dotenv_values()[_TOKEN_KEY]
    if BOT_TOKEN:
        main(BOT_TOKEN)
    else:
        logger.error("Couldn't obtain bot token from system environment")
