import functools
import logging

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from src.services import telegram_services

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_handlers() -> list:
    return [CommandHandler("start", start)]


def _response(text_func):
    @functools.wraps(text_func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = await text_func(update, context)
        await telegram_services.response(update, context, text)

    return wrapper


@_response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    logger.info(f"Command start by user {update.effective_user.username}")
    return "hi"
