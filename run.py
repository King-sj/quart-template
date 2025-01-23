from src import create_app
from config import parse_args
if __name__ == '__main__':
  args = parse_args()
  app = create_app()
  app.run(host=args.host, port=args.port)