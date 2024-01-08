# conftest.py
import os
import tempfile

import pytest
from flaskr import create_app
# from flaskr.db import get_db #, init_db

import os
import tempfile

import pytest
from flaskr import create_app, db

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# current_directory = os.path.dirname(os.path.abspath(__file__))
schema_path = os.path.join(parent_dir, 'flaskr', 'schema.sql')

with open(schema_path, 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app_context = app.app_context()
    app_context.push()
    yield app  # The testing client can access the app through this fixture
    app_context.pop()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def db(app):
    """Initialize and create the database for testing."""
    with app.app_context():
        db.create_all()
        yield db  # The test can access the database through this fixture
        db.session.remove()
        db.drop_all()
