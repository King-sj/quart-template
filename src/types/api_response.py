from typing import Any
class ApiResponse:
  '''
  ApiResponse class is a generic class for API response
  Attributes:
    res (Any): Response data
    err_msg (str): Error message outline
    err_code (str): Error code, default is '00000'
    err_msg_details (str): Error message details

  Methods:
    to_dict: Convert the object to dictionary
  '''

  def __init__(self, res:Any, err_msg: str = '',err_code: str = '00000',err_msg_details: str = ''):
    self.res = res
    self.err_msg = err_msg
    self.err_code = err_code
    self.err_msg_details = err_msg_details

  def to_dict(self):
    return {
      'res': self.res,
      'err-msg': self.err_msg,
      'err-code': self.err_code,
      'err-msg-details': self.err_msg_details
    }

class ApiException(Exception):
  '''
  ApiError class is a custom exception class for API error
  Attributes:
    err_msg (str): Error message
    err_code (str): Error code, default is '00000'
  '''
  def __init__(self, err_msg: str, err_code: str = '00000'):
    self.err_msg = err_msg
    self.err_code = err_code
    super().__init__(self.err_msg)