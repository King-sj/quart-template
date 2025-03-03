from idna import encode
from quart import Quart
from quart_cors import cors

from .args import parse_args
from .controllers import register_blueprints
from .auth import install_auth_module
from .configs import *
from tortoise.contrib.quart import register_tortoise
from redis import asyncio as aioredis
from redis.asyncio.client import Redis
from .globals import init_redis, get_redis, close_redis,Redis
from src.utils import generate_random_string

def init_check():
  '''
  Check if the environment is correctly set up
  '''
  env_cfg = EnvConfig()
  if env_cfg.TEST:
    raise Exception(
        "Do not run the app in test environment, you should run the tests and use test_app(in conftest) instead."
    )


def create_app():
  '''
  Create a Quart app
  '''
  args = parse_args()
  config = MainConfig()
  app = Quart(__name__,
              static_folder='../static',
              template_folder=config.TEMPLATE_DIR)

  app = cors(app, allow_origin=args.allow_origin)

  # To use tortoise-orm with Quart, you must call register_tortoise
  register_tortoise(
      app,
      db_url=config.DATABASE_URI,
      modules={'models': ['src.models']},
      generate_schemas=False,
  )

  register_blueprints(app)
  install_auth_module(app)

  app.secret_key = generate_random_string(32)

  @app.before_serving
  async def before_serving():
    await init_redis()

  @app.after_serving
  async def after_serving():
    await close_redis()

  return app
