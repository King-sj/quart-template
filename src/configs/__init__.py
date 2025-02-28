from dotenv import load_dotenv
import os
# 加载.env文件, 并且允许覆盖系统环境变量
load_dotenv(".env", override=True, verbose=True)
# 判断ENV环境变量是否存在, 如果不存在则默认为development
# 并再次加载.env文件, 以覆盖系统环境变量
if not os.getenv("ENV"):
  os.environ["ENV"] = "dev"
if os.getenv("ENV") == "dev":
  load_dotenv(".env.dev", override=True, verbose=True)
else:
  load_dotenv(".env.prod", override=True, verbose=True)

from .auth import Config as AuthConfig
from .main import Config as MainConfig
from .redis_prefix import Config as RedisPrefixConfig
from .logging import Config as LoggingConfig
from .email import Config as EmailConfig
from .env import Config as EnvConfig