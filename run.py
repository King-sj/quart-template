from flask import config
from src import create_app, parse_args, MainConfig, init_check
import logging
if __name__ == '__main__':

  init_check()

  logger = logging.getLogger(__name__)
  app = create_app()
  args = parse_args()

  config = MainConfig()

  logger.info(f'Author: {config.AUTHOR}')

  app.run(host=args.host, port=args.port, debug=args.debug)
