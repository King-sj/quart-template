from typing import Any
from tortoise import fields
from tortoise.models import Model


class User(Model):
  '''
  id 由 "雪花算法" 生成
  email 用户邮箱
  password 用户密码
  created_at 用户创建时间
  is_deleted 用户是否被删除
  deleted_at 用户删除时间
  role 用户角色
  name 用户姓名
  '''
  id = fields.BigIntField(pk=True)
  email = fields.CharField(max_length=255, unique=True)
  password = fields.CharField(max_length=255)
  created_at = fields.DatetimeField(auto_now_add=True)
  is_deleted = fields.BooleanField(default=False)
  deleted_at = fields.DatetimeField(null=True)
  role = fields.CharField(max_length=255, null=True)
  name = fields.CharField(max_length=255, null=True)

  def __repr__(self):
    return f'<User {self.email}>'
