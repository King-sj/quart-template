import pytest
from src import MainConfig
@pytest.mark.asyncio
async def test_index(client):
  config = MainConfig()
  response = await client.get('/')
  assert response.status_code == 200
  json_data = await response.get_json()
  assert json_data['message'] == 'Hello, Quart!'

@pytest.mark.asyncio
async def test_echo(client):
  test_data = {"key": "value"}
  config = MainConfig()
  response = await client.post('echo', json=test_data)
  assert response.status_code == 200
  json_data = await response.get_json()
  assert json_data == test_data