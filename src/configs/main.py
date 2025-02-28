import os

class Config:
  '''
  可以用.env文件来配置环境变量, 会自动读取
  '''
  def __init__(self):
    # 作者
    self.AUTHOR = os.getenv('AUTHOR', 'your_name')
    # 项目名
    self.PROJECT_NAME = os.getenv('PROJECT_NAME', 'your_project')
    # 项目描述
    self.PROJECT_DESC = os.getenv('PROJECT_DESC', 'your_project_desc')
    # 项目版本
    self.PROJECT_VERSION = os.getenv('PROJECT_VERSION', '0.0.1')

    self.REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    self.POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE', 'postgres')
    self.POSTGRES_USER = os.getenv('POSTGRES', 'postgres')
    self.POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
    self.POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    self.POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)

    self.DB_POOL_MIN_SIZE = os.getenv('DB_POOL_MIN_SIZE', 1)
    self.DB_POOL_MAX_SIZE = os.getenv('DB_POOL_MAX_SIZE', 16)
    self.DB_ECHO = os.getenv('DB_ECHO', False)
    self.DB_SSL = os.getenv('DB_SSL', False)
    self.DB_USE_CONNECTION_FOR_REQUEST = os.getenv('DB_USE_CONNECTION_FOR_REQUEST', True)
    self.DB_RETRY_LIMIT = os.getenv('DB_RETRY_LIMIT', 10)
    self.DB_RETRY_INTERVAL = os.getenv('DB_RETRY_INTERVAL', 1)

    self.DATABASE_URI = f'postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}'
    self.DATABASE_URI = os.getenv('DATABASE_URI', self.DATABASE_URI)


    self.URL_PREFIX = os.getenv('URL_PREFIX', '/api/v1/')

    self.TEMPLATE_DIR = os.getenv('TEMPLATE_DIR', '../templates')
