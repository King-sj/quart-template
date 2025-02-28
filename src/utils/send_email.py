__all__ = ['send_email']
import ssl
import aiosmtplib
from quart import render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..configs import EmailConfig


async def send_email(to: str, subject: str, body: str, username: str = "用户"):
  '''
  发送邮件

  :param to: 收件人
  :param subject: 主题
  :param body: 内容
  :return: None

  Example:
  ```python
  await send_email('test@qq.com','test','test')
  ```
  '''

  html_body = await render_template(r"email.html", user=username, msg=body)
  # add check for "to" email address
  cfg = EmailConfig()

  msg = MIMEMultipart('alternative')
  msg['From'] = cfg.MAIL_DEFAULT_SENDER
  msg['To'] = to
  msg['Subject'] = subject
  msg.attach(MIMEText(html_body, 'html'))
  # 异步发送邮件
  async with aiosmtplib.SMTP(
      hostname=cfg.MAIL_SERVER,
      port=int(cfg.MAIL_PORT),
  ) as smtp:
    # if bool(cfg.MAIL_USE_TLS):
    #   await smtp.starttls()
    await smtp.login(cfg.MAIL_USERNAME, cfg.MAIL_PASSWORD)
    res = await smtp.send_message(msg)
    if not res:
      raise Exception('exist email send failed')
    return res

