from quart import Quart, request, jsonify
from quart_cors import cors
from config import parse_args
from src.routes import *

def create_app():
  args = parse_args()
  app = Quart(__name__)
  app = cors(app, allow_origin=args.allow_origin)
  app.register_blueprint(main_bp)
  return app

if __name__ == '__main__':
  args = parse_args()
  app = create_app()
  app.run(host=args.host, port=args.port)