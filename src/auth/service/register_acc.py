from ..types import RegisterRequest
from src.globals import get_redis
from src.configs import AuthConfig, RedisPrefixConfig
from .token import generate_token_and_store,generate_refresh_token_and_store
from src.models import User
from src.utils import SnowFlake
from ..utils import encrypt_psw

async def register_account(data: RegisterRequest):
  '''
  Register a new account
  :param data: RegisterRequest data
  :return: dict
    user-id (int): User ID
    token  (str): Token
  '''
  # 验证验证码
  redis = await get_redis()
  cfg = AuthConfig()
  key = RedisPrefixConfig().EMAIL2CAPTCHA + data.account
  async with redis.client() as conn:
    captcha = await conn.get(key)
    if not captcha:
      raise Exception('Captcha is expired')
    if captcha.decode() != data.captcha:
      raise Exception('Captcha is not right')
  # 检查用户是否存在
  user = await User.get_or_none(email=data.account)
  if user:
    raise Exception('User already exists')
  # 创建用户
  psw = encrypt_psw(data.psw,cfg.SALT_LENGTH)
  user = User(id=SnowFlake().gen_id(),
              email=data.account,
              password=psw,
              role='user',
              name=data.account)
  await user.save()
  # 生成token
  token = await generate_token_and_store(user.id)
  # 生成refresh token
  refresh_token = await generate_refresh_token_and_store(user.id)
  res = {
    'user-id': user.id,
    'token': token,
    'refresh-token': refresh_token
  }
  return res