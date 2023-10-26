import logging

from telegram.ext import ApplicationBuilder

from src.handlers.bot_handlers import get_handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token):
        self.TOKEN = token
        self.application = ApplicationBuilder().token(self.TOKEN).build()
        handlers = get_handlers()
        self._initialize_handlers(handlers)

    def _initialize_handlers(self, handlers):
        for handler in handlers:
            self.application.add_handler(handler)

    def run_polling(self):
        logger.info("Starting bot in polling mode")
        self.application.run_polling()
