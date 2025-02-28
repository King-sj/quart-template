from src.globals import get_redis
from src.configs import AuthConfig, RedisPrefixConfig
import uuid


async def generate_token_and_store(user_id: int):
  '''
  Generate a token and store it in redis
  :param user_id: int
  :return: str
  '''
  redis = await get_redis()
  cfg = AuthConfig()

  # 生成不重复 token

  token = uuid.uuid4().hex

  async with redis.client() as conn:
    # 删除旧的token
    old_token = await conn.get(RedisPrefixConfig().USERID2TOKEN + str(user_id))

    if old_token:
      old_token = old_token.decode()
      await conn.delete(RedisPrefixConfig().TOKEN2USERID + old_token)
    # update
    await conn.setex(RedisPrefixConfig().TOKEN2USERID + token,
                     cfg.TOKEN_EXPIRE, str(user_id))
    await conn.setex(RedisPrefixConfig().USERID2TOKEN + str(user_id),
                     cfg.TOKEN_EXPIRE, token)
  return token


async def refresh_token(user_id: int, token: str, refresh_token: str) -> str:
  '''
  Refresh token
  :param user_id: int
  :param token: str
  :param refresh_token: str
  :return: str
  '''

  redis = await get_redis()
  # 验证 token 和 refresh_token
  async with redis.client() as conn:
    # 验证token
    token_key = RedisPrefixConfig().TOKEN2USERID + token
    userid = await conn.get(token_key)
    if not userid:
      raise Exception('Token is invalid')
    userid = int(userid)
    if userid != user_id:
      raise Exception('Token is Error')
    # 验证refresh_token
    refresh_token_key = RedisPrefixConfig().REFRESH_TOKEN2USERID + refresh_token
    userid = await conn.get(refresh_token_key)
    if not userid:
      raise Exception('Refresh token is invalid')
    userid = int(userid)
    if userid != user_id:
      raise Exception('Refresh token is error')

  # 生成新的token
  new_token = await generate_token_and_store(user_id)
  return new_token


async def generate_refresh_token_and_store(user_id: int):
  '''
  Generate a refresh token and store it in redis
  :param user_id: int
  :return: str
  '''
  redis = await get_redis()
  cfg = AuthConfig()

  # 生成不重复 token

  token = uuid.uuid4().hex


  async with redis.client() as conn:
    # 删除旧的refresh_token
    old_token = await conn.get(RedisPrefixConfig().USERID2REFRESH_TOKEN + str(user_id))
    if old_token:
      old_token = old_token.decode()
      await conn.delete(RedisPrefixConfig().REFRESH_TOKEN2USERID + old_token)
    # update
    await conn.setex(RedisPrefixConfig().REFRESH_TOKEN2USERID + token, cfg.REFRESH_TOKEN_EXPIRE, str(user_id))
    await conn.setex(RedisPrefixConfig().USERID2REFRESH_TOKEN + str(user_id), cfg.REFRESH_TOKEN_EXPIRE, token)
  return token
