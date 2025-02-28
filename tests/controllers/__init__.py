__all__ = ['register_blueprints']
from .main import main_bp
from quart import Quart

def register_blueprints(app: Quart) -> None:
  '''
  Register all test blueprints for the app.

  Args:
    app (Quart): The app to register the blueprints to.
  '''
  app.register_blueprint(main_bp, url_prefix='/test/main')