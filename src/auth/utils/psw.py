__all__ = ['encrypt_psw', 'verify_psw']
from src.utils import generate_random_string
import hashlib

def hash_password(psw, salt):
  '''
  Hash password

  :param psw: password

  :param salt: salt

  :return: hashed password
  '''
  psw = psw + salt
  psw = hashlib.md5(psw.encode()).hexdigest()
  return psw


# 密码加密
def encrypt_psw(psw: str , salt_length: int = 16):
  '''
  Encrypt password

  :param psw: password

  :return: encrypted salt+password
  '''
  salt = generate_random_string(salt_length)
  psw = hash_password(psw, salt)
  return salt+psw

# 密码验证
def verify_psw(psw: str, psw_cipher: str, salt: str):
  '''
  Verify password

  :param psw: password plain text

  :param psw_cipher: password cipher text (contains salt)

  :param salt: salt

  :return: True if password is correct, else False
  '''
  psw = hash_password(psw, salt)
  psw = salt + psw
  return psw == psw_cipher