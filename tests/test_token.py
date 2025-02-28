import pytest
from src.configs import AuthConfig

@pytest.mark.asyncio
async def test_token_missing(app):
  test_client = app.test_client()
  response = await test_client.get('/test/main/protected')
  assert response.status_code == 403
  json_data = await response.get_json()
  assert json_data['err-msg'] == 'Token is required'


@pytest.mark.asyncio
async def test_token_present(app):
  test_client = app.test_client()
  cfg = AuthConfig()
  headers = {cfg.AUTH_KEY: f'{cfg.AUTH_HEADER} test_token'}
  response = await test_client.get('/test/main/protected', headers=headers)
  assert response.status_code == 200
  json_data = await response.get_json()
  assert json_data['message'] == 'Success'
  assert json_data['userid'] == -1
  assert json_data['token'] == 'test_token'
