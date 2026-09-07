import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Handler 1: console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

# Handler 2: arquivo
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("mensagem de debug")
logger.info("mensagem de info")
logger.warning("mensagem de warning")
logger.error("mensagem de error")

