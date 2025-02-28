from src.configs import *
from src.globals import get_redis
from src.configs import RedisPrefixConfig

async def logout(token: str):
  '''
  Logout
  '''
  # delete token cache
  key = RedisPrefixConfig().TOKEN2USERID+token
  redis = await get_redis()
  async with redis.client() as conn:
    await conn.delete(key)
