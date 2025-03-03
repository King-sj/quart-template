__all__ = ['main_bp']
from quart import Blueprint, request, jsonify, session
from src.types import ApiResponse
main_bp = Blueprint('main', __name__, static_folder='../../static')


@main_bp.route('/')
async def index():
  return jsonify({"message": "Hello, Quart!"})


@main_bp.route('/echo', methods=['POST'])
async def echo():
  data = await request.get_json()
  return jsonify(data)


@main_bp.get('/err-code')
async def get_error_code_table():
  '''
  Get the error code table in markdown format
  '''
  return await main_bp.send_static_file('err-code-table.zh.md')

# session example
# should set app.secret_key before using session
@main_bp.get('/set_session/<key>/<value>')
async def set_session(key, value):
  session[key] = value
  res = ApiResponse(f"session set {key}={value}")
  return jsonify(res.to_dict())

@main_bp.get('/get_session/<key>')
async def get_session(key):
  value = session.get(key)
  res = ApiResponse(f"session get {key}={value}")
  return jsonify(res.to_dict())