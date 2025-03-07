from functools import wraps
from quart import request, jsonify
from src.types import ApiResponse
from typing import Any

def validate_request(schema:Any,method:str='POST'):
  '''
  Validate request body with pydantic schema

  Args:

    schema : pydantic schema

    method (str, optional): request method. Defaults to 'POST'. ['POST', 'GET']

  DecoratorFuncArgs:
    validated_data : validated data

  Example:

  ```python
    @app.post('/url')
    @validate_request(ActivityRequest)
    async def update_activities(validated_data: ActivityRequest):
        activity = validated_data  # 直接使用验证后的数据
  ```
  '''

  def decorator(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
      try:
        if method == 'POST':
          data = await request.get_json()
        elif method == 'GET':
          data = request.args.to_dict()
        else :
          raise ValueError('Invalid method, now just support POST and GET')
        validated_data = schema(**data)  # type: ignore
      except Exception as e:
        return jsonify(
            ApiResponse(None, 'Invalid request body', 'A0400',
                        str(e)).to_dict()), 400
      return await func(*args, validated_data=validated_data, **kwargs)

    return wrapper

  return decorator
