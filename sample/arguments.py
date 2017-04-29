import sys
import logging
from logging import StreamHandler


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.debug('LENGTH:' + str(len(sys.argv)))
logger.debug('ARGV:' + str(sys.argv))
