import pytest
@pytest.mark.asyncio
async def test_index(client):
  response = await client.get('/')
  assert response.status_code == 200
  json_data = await response.get_json()
  assert json_data['message'] == 'Hello, Quart!'