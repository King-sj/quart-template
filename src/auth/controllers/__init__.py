__all__ = ['register_blueprints']
from .main import main_bp
from quart import Quart
from ...configs import MainConfig

def register_blueprints(app: Quart):
  '''
  Register auth module blueprints to the app
  '''
  cfg = MainConfig()
  app.register_blueprint(main_bp,url_prefix=cfg.URL_PREFIX+'auth/')
