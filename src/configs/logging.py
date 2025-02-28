'''
  logging config
'''
import os
class Config:
  def __init__(self) -> None:
    self.ENABLE_FILE_LOG = os.getenv('ENABLE_FILE_LOG', True)
    self.LOG_DIR = os.getenv('LOG_DIR', 'logs')
    self.LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
