import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s"
))
logger.addHandler(handler)

def processar_backup():
    logger.info("processando backup")

processar_backup()
