from src.globals import get_redis
from src.configs import AuthConfig, RedisPrefixConfig
from src.utils import generate_random_string, send_email


async def generate_and_store_captcha(account: str) -> str:
  '''
  Generate a captcha , store it to redis, and send it to the account

  :param account: Account, now just support email address
  :return: Captcha
  '''
  cfg = AuthConfig()
  captcha = generate_random_string(cfg.CAPTCHA_LEN)
  redis = await get_redis()
  key = RedisPrefixConfig().EMAIL2CAPTCHA + account
  async with redis.client() as conn:
    await conn.setex(key, cfg.CAPTCHA_EXPIRE, captcha)
  # send email
  await send_email(account, 'Register captcha', f'Your captcha is {captcha}')
  return captcha
