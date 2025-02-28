from ..configs import LoggingConfig
from .logging import setup_logging

logging_config = LoggingConfig()

if logging_config.ENABLE_FILE_LOG:
  setup_logging()
  print('\033[91m' + "setup logging module done" + '\033[0m')
