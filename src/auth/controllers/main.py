__all__ = ['main_bp']
from quart import Blueprint, jsonify
from src.auth import token_required
from src.models import User
from src.controllers.main import main_bp
from src.types import ApiResponse
from quart import request
from src.configs import *
from ..types import CaptchaRequest, RegisterRequest, LoginRequest, RefreshTokenRequest
# from pydantic import ValidationError
from ..service import register_account, login, logout, refresh_token, generate_and_store_captcha


main_bp = Blueprint('auth_main', __name__)


@main_bp.post('/captcha')
async def get_captcha():
  '''
  Get a captcha, and store it to redis

  Request:
    type (str): Account type, now just support 'email'
    account (str): Account, now just support email address

  Response:
    res (str): Captcha

  '''
  data = await request.get_json()
  try:
    data = CaptchaRequest(**data)
  except Exception as e:
    res = ApiResponse(None, 'request data is not right', 'A0402', repr(e))
    return jsonify(res.to_dict()), 400

  acc_type = data.type
  if acc_type != 'email':
    res = ApiResponse(None, 'Now just support Email', 'A0001')
    return jsonify(res.to_dict()), 400

  await generate_and_store_captcha(data.account)
  res = ApiResponse("captcha has been sent to your email")
  return jsonify(res.to_dict())


@main_bp.post('/register')
async def register_acc():
  data = await request.get_json()
  try:
    data = RegisterRequest(**data)
  except Exception as e:
    res = ApiResponse(None, 'request data is not right', 'A0402', repr(e))
    return jsonify(res.to_dict()), 400

  acc_type = data.type
  if acc_type != 'email':
    res = ApiResponse(None, 'Now just support Email', 'A0001')
    return jsonify(res.to_dict()), 400

  try:
    res = await register_account(data)
  except Exception as e:
    res = ApiResponse(None, 'register failed', 'B0001', repr(e))
    return jsonify(res.to_dict()), 400
  res = ApiResponse(res)
  return jsonify(res.to_dict())


@main_bp.post('/login')
async def login_controller():
  data = await request.get_json()
  try:
    data = LoginRequest(**data)
  except Exception as e:
    res = ApiResponse(None, 'request data is not right', 'A0402', repr(e))
    return jsonify(res.to_dict()), 400

  acc_type = data.type
  if acc_type != 'email':
    res = ApiResponse(None, 'Now just support Email', 'A0001')
    return jsonify(res.to_dict()), 400

  try:
    res = await login(data)
  except Exception as e:
    res = ApiResponse(None, 'login failed', 'B0001', repr(e))
    return jsonify(res.to_dict()), 400
  res = ApiResponse(res)
  return jsonify(res.to_dict())


@main_bp.get('/logout')
@token_required()
async def logout_controller(token: str, userid: int):
  await logout(token)
  res = ApiResponse('Logout successfully')
  return jsonify(res.to_dict())


@main_bp.post('/refresh-token')
@token_required()
async def refresh_token_controller(token: str, userid: int):
  '''
  Refresh token

  需要在token过期前调用,否则会返回401

  同时需要TOKEN和REFRESH_TOKEN
  '''
  # TODO: 添加流量控制，防止刷接口
  data = await request.get_json()
  try:
    data = RefreshTokenRequest(**data)
  except Exception as e:
    res = ApiResponse(None, 'request data is not right', 'A0402', repr(e))
    return jsonify(res.to_dict()), 400
  try:
    res = await refresh_token(userid, token, data.refresh_token)
  except Exception as e:
    res = ApiResponse(None, 'refresh token failed', 'B0001', repr(e))
    return jsonify(res.to_dict()), 400
  res = ApiResponse(res)
  return jsonify(res.to_dict())
