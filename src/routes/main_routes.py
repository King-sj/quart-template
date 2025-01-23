__all__ = ['main_bp']
from quart import Blueprint, jsonify, request

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
async def index():
  return jsonify({"message": "Hello, Quart!"})

@main_bp.route('/echo', methods=['POST'])
async def echo():
  data = await request.get_json()
  return jsonify(data)