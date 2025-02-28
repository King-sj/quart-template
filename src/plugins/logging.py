import logging
import logging.config
import os
from ..configs import LoggingConfig


def setup_logging():
  '''
  setup logging config
  '''
  config = LoggingConfig()
  log_dir = config.LOG_DIR
  log_level = config.LOG_LEVEL

  if not os.path.exists(log_dir):
    os.makedirs(log_dir)

  logging_config = {
      'version': 1,
      'disable_existing_loggers': False,
      'formatters': {
          'detailed': {
              'format':
              '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
          },
          'standard': {
              'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
          },
      },
      'handlers': {
          'console': {
              'level': 'DEBUG',
              'class': 'logging.StreamHandler',
              'formatter': 'standard',
          },
          'file_debug': {
              'level': 'DEBUG',
              'class': 'logging.FileHandler',
              'filename': os.path.join(log_dir, 'app_debug.log'),
              'formatter': 'detailed',
          },
          'file_info': {
              'level': 'INFO',
              'class': 'logging.FileHandler',
              'filename': os.path.join(log_dir, 'app_info.log'),
              'formatter': 'detailed',
          },
          'file_warning': {
              'level': 'WARNING',
              'class': 'logging.FileHandler',
              'filename': os.path.join(log_dir, 'app_warning.log'),
              'formatter': 'detailed',
          },
          'file_error': {
              'level': 'ERROR',
              'class': 'logging.FileHandler',
              'filename': os.path.join(log_dir, 'app_error.log'),
              'formatter': 'detailed',
          },
      },
      'loggers': {
          '': {
              'handlers': [
                  'console', 'file_debug', 'file_info', 'file_warning',
                  'file_error'
              ],
              'level':
              'DEBUG',
              'propagate':
              True,
          },
      }
  }

  logging.config.dictConfig(logging_config)
  logging.basicConfig(level=log_level,force=True)
