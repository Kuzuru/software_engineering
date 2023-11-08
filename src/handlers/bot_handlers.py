import functools
import logging

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from src.services import telegram_services
from src.services.forecast_service import get_forecast
from src.utils.text import INSTRUCTION, WRONG_ARGUMENTS

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_handlers() -> list:
    return [CommandHandler("start", start),
            CommandHandler("forecast", forecast)]


def _response(text_func):
    @functools.wraps(text_func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = await text_func(update, context)
        await telegram_services.response(update, context, text)

    return wrapper


@_response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    logger.info(f"Command start by user {update.effective_user.username}")
    return INSTRUCTION


@_response
async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    logger.info(f"Command forecast by user {update.effective_user.username}")
    args = context.args
    # if not await are_args_valid(args):
    #     return WRONG_ARGUMENTS
    ticket, n_day = args
    result = await get_forecast(ticket, n_day)
    return result
