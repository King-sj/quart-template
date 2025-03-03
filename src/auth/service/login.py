from ..types import LoginRequest
from src.models import User
from .token import generate_token_and_store, generate_refresh_token_and_store
from ..utils import verify_psw
from src.configs import AuthConfig

async def login(data: LoginRequest):
  '''
  Login service
  :param data: LoginRequest
  '''
  # 验证登陆信息
  user = await User.get_or_none(email=data.account)
  if user is None:
    raise Exception('account does not exist')
  cfg = AuthConfig()
  salt = user.password[:cfg.SALT_LENGTH]
  if verify_psw(data.psw, user.password, salt) is False:
    raise Exception('password is not correct')
  token = await generate_token_and_store(user.id)

  refresh_token = await generate_refresh_token_and_store(user.id)

  return {'token': token, 'user-id': user.id, 'refresh-token': refresh_token}
