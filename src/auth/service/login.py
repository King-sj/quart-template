from ..types import LoginRequest
from src.models import User
from .token import generate_token_and_store, generate_refresh_token_and_store


async def login(data: LoginRequest):
  '''
  Login service
  :param data: LoginRequest
  '''
  # 验证登陆信息
  user = await User.get_or_none(email=data.account)
  if user is None:
    raise Exception('account does not exist')
  if user.password != data.psw:
    raise Exception('password is not correct')

  token = await generate_token_and_store(user.id)

  refresh_token = await generate_refresh_token_and_store(user.id)

  return {'token': token, 'user-id': user.id, 'refresh-token': refresh_token}
