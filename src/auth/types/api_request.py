from pydantic import BaseModel


class CaptchaRequest(BaseModel):
  '''
  Captcha request data

  Attributes:
    type (str): Account type, now just support 'email'
    account (str): Account, now just support email address
  '''
  type: str
  account: str

class RegisterRequest(BaseModel):
  '''
  Register request data

  Attributes:
    type (str): Account type, now just support 'email'
    account (str): Account, now just support email address
    psw (str): Password
    captcha (str): Captcha
  '''
  type: str
  account: str
  psw: str
  captcha: str

class LoginRequest(BaseModel):
  '''
  Login request data

  Attributes:
    type (str): Account type, now just support 'email'
    account (str): Account, now just support email
    psw (str): Password
  '''
  type: str
  account: str
  psw: str

class RefreshTokenRequest(BaseModel):
  '''
  Refresh token request data

  Attributes:
    refresh_token (str): Refresh token
  '''
  refresh_token: str