__all__ = ['register_blueprints']
from .main import main_bp
from quart import Quart

def register_blueprints(app: Quart):
  '''
  Register blueprints to the app
  '''
  app.register_blueprint(main_bp)
