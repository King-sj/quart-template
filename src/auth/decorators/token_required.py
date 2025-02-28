from math import log
from venv import logger
from quart import request, jsonify
from src.globals import get_redis
from src.configs import AuthConfig,RedisPrefixConfig
import logging
from functools import wraps

from src.types.api_response import ApiResponse
logger = logging.getLogger(__name__)
def token_required(test=False):
  '''
  Decorator to check if the request has a valid token

  you can get the <userid> and <token> in the decorated function

  Token style(default, can be changed):

  Authorization: <认证方案> <凭证信息>

  @param test: bool, default False, if True, return -1 as userid for any existing token

  Examples:
  ```python
  @app.route('/a-protected-route')
  @token_required()
  # attention: userid is passed as a keyword argument to the decorated function
  async def protected(userid,token):
    print(f'protected:Success with userid: {userid}')
  ```
  '''

  def decorated(func):
    # wraps 用于修复func的名字和docstring被装饰器覆盖的问题
    @wraps(func)
    async def wrapped(*args, **kwargs):
      try:
        cfg = AuthConfig()
        # 自己实现的headers: token验证逻辑
        token = request.headers.get(cfg.AUTH_KEY)
        token = token.split(' ')[-1] if token else None
        if not token:
          res = ApiResponse(None, 'Token is required', 'A0410')
          return jsonify(res.to_dict()), 403
        # for pytest or other test cases, return -1 as userid
        userid = -1
        if test:
          return await func(*args, **kwargs, userid=userid, token=token)

        redis = await get_redis()
        key = RedisPrefixConfig().TOKEN2USERID + token
        async with redis.client() as conn:
          userid = await conn.get(key)
          if not userid:
            res = ApiResponse(None, 'Token is invalid', 'A0411')
            return jsonify(res.to_dict()), 403
          # bytes to int
          userid = int(userid)

        # 将userid以 userid=<userid> 的kwargs传递给被装饰的函数
        return await func(*args, **kwargs, userid=userid, token=token)
      except Exception as e:
        logger.error(f'Error in token_required: {repr(e)}')
        res = ApiResponse(None, 'Internal Error', 'B0001', repr(e))
        return jsonify(res.to_dict()), 500
    return wrapped
  return decorated
