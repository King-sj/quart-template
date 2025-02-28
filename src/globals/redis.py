__all__ = ['init_redis', 'get_redis', 'close_redis','Redis']
from re import M
from venv import logger
from redis import asyncio as aioredis
from redis.asyncio.client import Redis
from src.configs import MainConfig
import logging
from asyncio import Lock

redis = None
logger = logging.getLogger(__name__)
log_lock = Lock()

async def init_redis() -> Redis:
  global redis
  cfg = MainConfig()
  redis = aioredis.from_url(cfg.REDIS_URL, encoding='utf-8')
  async with log_lock:
    logger.info('init redis done')
  return redis

async def get_redis() -> Redis:
  global redis
  if redis is None:
    raise Exception('Redis connection is not established')
  return redis

async def close_redis():
  global redis
  if redis is None:
    raise Exception('Redis connection is not established')
  await redis.close()
  redis = None
  async with log_lock:
    logger.info('redis have closed')