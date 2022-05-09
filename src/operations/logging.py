import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.CRITICAL)
logger.addHandler(handler)