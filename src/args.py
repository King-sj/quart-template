import argparse


def parse_args():
  args = argparse.ArgumentParser(description='Quart Websocket Server')

  args.add_argument('--host', type=str, default='localhost', help='Host')

  args.add_argument('--port', type=int, default=5000, help='Port')

  args.add_argument('--debug', type=bool, default=True, help='Debug')

  args.add_argument('--ssl', type=bool, default=False, help='SSL')

  args.add_argument('--ssl_keyfile',
                    type=str,
                    default=None,
                    help='SSL Keyfile')

  args.add_argument('--ssl_certfile',
                    type=str,
                    default=None,
                    help='SSL Certfile')

  args.add_argument('--allow_origin',
                    type=str,
                    default='*',
                    help='Allow Origin')
  # 用于解决: 使用 pytest tests 进行测试时， 会意外识别到 tests 参数， 导致错误
  args, _ = args.parse_known_args()
  return args
