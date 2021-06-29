import pytest
import os
from app import app as flask_app

token = os.getenv('token')
key = os.getenv('key')

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()