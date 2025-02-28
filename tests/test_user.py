'''
这种会报错InterfaceError('cannot perform operation: another operation is in progress')

@pytest.mark.asyncio
async def test_user(client):

'''
import pytest
from src.models import User
from src.utils import SnowFlake
import asyncio


def test_user(client):

  async def inner():
    res = await client.get('/test/main/test-user')
    if res.status_code != 200:
      print("test_user res:",res)
    assert res.status_code == 200
    json = await res.get_json()
    assert json['message'] == 'User created successfully'
    id = json['res']['id']
    user = await User.get(id=id)
    assert user
    assert user.id == id
    assert user.email
    assert user.password
    assert user.role
    assert user.name
    assert user.created_at

  asyncio.get_event_loop().run_until_complete(inner())
