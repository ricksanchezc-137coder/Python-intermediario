import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.debug("mensagem de debug")
logger.info("mensagem de info")
logger.warning("mensagem de warning")
logger.error("mensagem de error")
logger.critical("mensagem de critical")

