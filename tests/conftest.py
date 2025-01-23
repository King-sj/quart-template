# content of tests/conftest.py
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
print(sys.path)

import pytest
from src import create_app

@pytest.fixture
def app():
  app = create_app()
  return app

@pytest.fixture
def client(app):
  return app.test_client()