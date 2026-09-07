import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    "rotativo.log",
    maxBytes=200, # bem pequeno, só pra forçar rotação rápido no teste
    backupCount=3
)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

for i in range(30):
    logger.info(f"linha de log numero {i}")

