# content of tests/conftest.py
from operator import ge
import os
from re import I
import sys
from dotenv import load_dotenv
import pytest_asyncio
import asyncio
# add the project path to sys.path, to solve the problem of module not found
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
print(sys.path)
from src.configs import MainConfig, EnvConfig
import pytest
from src import create_app
from utils import *
from tortoise import Tortoise, connections
from controllers import register_blueprints


@pytest.fixture
def app(scope="session"):
  app = create_app()
  register_blueprints(app)
  return app


@pytest.fixture
def client(app, scope="function"):
  return app.test_client()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def global_async_fixture():
  # will run before any test
  await async_setup()
  yield
  # will run after all tests
  await async_teardown()  # type: ignore


@pytest.yield_fixture(scope="function")
def event_loop():
  print("\n=== 初始化事件循环===")
  policy = asyncio.get_event_loop_policy()
  loop = policy.new_event_loop()
  yield loop
  print("\n=== 清理事件循环===")
  loop.close()


async def async_setup():
  print("\n=== 异步初始化===")
  # Load the .env.test file to override the default settings in .env/.env.dev/.env.prod
  load_dotenv(".env.test", override=True, verbose=True)

  cfg = EnvConfig()
  # 检查是否正确导入了 .env.test 文件
  if not cfg.TEST:
    raise Exception("未正确导入 .env.test 文件")

  await Tortoise.init(
      db_url=MainConfig().DATABASE_URI,
      modules={'models': ['src.models']},
  )
  await Tortoise.generate_schemas()


async def async_teardown():
  print("\n=== 异步清理 ===")
  #Tortoise 删除所有table, 但是不删除database
  await drop_all_tables()
  await Tortoise.close_connections()
