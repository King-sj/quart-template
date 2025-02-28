from src.utils import send_email
from src.configs import EmailConfig
import asyncio
import pytest

def test_send_email(app):

  async def inner():
    # 手动推送应用上下文
    async with app.app_context():
      cfg = EmailConfig()

      acc = cfg.TEST_EMAIL_ACCOUNT
      sbj = cfg.TEST_EMAIL_SUBJECT
      bdy = cfg.TEST_EMAIL_BODY

      if acc == '':
        raise Exception("未配置测试邮箱")

      # 在应用上下文中执行发送
      try:
        await send_email(acc, sbj, bdy)
        assert True
      except Exception as e:
        assert False, f"邮件发送失败: {str(e)}"

  # 使用 Quart 应用的异步循环
  # app.loop.run_until_complete(inner())
  asyncio.get_event_loop().run_until_complete(inner())


@pytest.mark.asyncio
async def test_send_email_url(client):
  res = await client.get('/test/main/test-email')
  assert res.status_code == 200
  json = await res.get_json()
  assert json['message'] == 'Email sent successfully'
