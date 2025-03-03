'''
鉴权相关配置
'''
import os

class Config:
  '''
  鉴权相关配置
  TOKEN默认过期时间 0.5day, 单位秒

  CAPTCHA 默认过期时间 5min, 单位s
  '''
  def __init__(self):
    self.TOKEN_EXPIRE:int = int(os.getenv('TOKEN_EXPIRE', 60*60*12))

    # 弃用，暂采用uuid
    # self.TOKEN_LENGTH:int = int(os.getenv('TOKEN_LENGTH', 32))

    self.REFRESH_TOKEN_EXPIRE:int = int(os.getenv('REFRESH_TOKEN_EXPIRE', 60*60*24*7)) # 7 days
    # 弃用，暂采用uuid
    # self.REFRESH_TOKEN_LENGTH:int = int(os.getenv('REFRESH_TOKEN_LENGTH', 32))

    self.CAPTCHA_EXPIRE:int = int(os.getenv('CAPTCHA_EXPIRE',60*5))
    self.CAPTCHA_LEN:int=int(os.getenv('CAPTCHA_LEN',6))

    # Authorization: <认证方案> <凭证信息>
    # 认证方案: Customize,Basic,Bearer
    self.AUTH_KEY = os.getenv('AUTH_KEY','Authorization')
    self.AUTH_HEADER:str = os.getenv('AUTH_HEADER', 'Customize')

    # 密码加密salt length
    self.SALT_LENGTH:int = int(os.getenv('SALT_LENGTH', 32))