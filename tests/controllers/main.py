__all__ = ['main_bp']
import email
import re
from quart import Blueprint, request, jsonify

main_bp = Blueprint('test_main', __name__, static_folder='../../static')

from src.utils import send_email
from src.auth import token_required
from src.models import User
from src.utils import SnowFlake
from src.configs import EmailConfig


@main_bp.get('/test-email')
async def _():
  cfg = EmailConfig()

  acc = cfg.TEST_EMAIL_ACCOUNT
  sbj = cfg.TEST_EMAIL_SUBJECT
  bdy = cfg.TEST_EMAIL_BODY

  if acc == '':
    raise Exception("未配置测试邮箱")

  res = await send_email(acc, sbj, bdy)

  return jsonify({'message': 'Email sent successfully', 'response': res})


@main_bp.route('/protected')
@token_required(test=True)
async def protected(userid,token):
  return jsonify({'message': 'Success', 'userid': userid, 'token': token})


@main_bp.route('/test-user')
async def test_user():
  try:
    user = User(id=SnowFlake().gen_id(),
                email='test@gmail.com',
                password='test',
                role='user',
                name='test')
    await user.save()
  except Exception as e:
    return jsonify({'message': str(e)}), 500
  return jsonify({
      'message': 'User created successfully',
      'res': {
          'id': user.id
      }
  }), 200
