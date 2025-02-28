import os

class Config:
  '''
  邮件配置
  '''
  def __init__(self) -> None:
    self.MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.163.com')
    self.MAIL_PORT = int(os.getenv('MAIL_PORT', 25))
    self.MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your_username')
    self.MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your_password')
    self.MAIL_USE_TLS = bool(os.getenv('MAIL_USE_TLS', False))
    self.MAIL_USE_SSL = bool(os.getenv('MAIL_USE_SSL', False))
    self.MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'your_email')
    self.MAIL_ADMIN = os.getenv('MAIL_ADMIN', 'admin_email')
    self.TEST_EMAIL_ACCOUNT = os.getenv('TEST_EMAIL_ACCOUNT', '')
    self.TEST_EMAIL_SUBJECT = os.getenv('TEST_EMAIL_SUBJECT', 'test subject')
    self.TEST_EMAIL_BODY = os.getenv('TEST_EMAIL_BODY', 'test body')

