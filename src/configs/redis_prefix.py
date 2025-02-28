'''
  redis prefix
'''

import os

class Config:
  '''
  redis prefix config
  '''
  def __init__(self):
    # email to captcha
    self.EMAIL2CAPTCHA = os.getenv('EMAIL_CAPTCHA_PREFIX', 'auth:email2captcha:')
    # token to userid
    self.TOKEN2USERID = os.getenv('TOKEN_USERID_PREFIX', 'auth:token2userid:')
    self.USERID2TOKEN = os.getenv('USERID_TOKEN_PREFIX', 'auth:userid2token:')

    # refresh token to userid
    self.REFRESH_TOKEN2USERID = os.getenv('REFRESH_TOKEN_USERID_PREFIX', 'auth:refresh_token2userid:')
    self.USERID2REFRESH_TOKEN = os.getenv('USERID_REFRESH_TOKEN_PREFIX', 'auth:userid2refresh_token:')
    # 暂时无用
    # userid is login
    # self.USERID_LOGIN = os.getenv('USERID_LOGIN_PREFIX', 'auth:userid_login:')