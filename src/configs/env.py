import os

class Config:
  '''
  可以用.env文件来配置环境变量, 会自动读取

  ENV: ['dev','prod']
  '''
  def __init__(self) -> None:
    self.ENV = os.getenv("ENV", "dev")
    self.DEBUG = os.getenv("DEBUG", True)
    self.TEST = bool(os.getenv("TEST", False))