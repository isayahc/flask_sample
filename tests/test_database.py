# test_database.py
import unittest
# from . import create_app, db
# from .models import User

from flaskr import create_app, db
from flaskr.models import User

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_user(self):
        response = self.client.get('/user/testuser')
        self.assertEqual(response.status_code, 404)

        # Add a user to the in-memory testing database
        user = User(username='testuser')
        db.session.add(user)
        db.session.commit()

        # Retrieve the added user
        response = self.client.get('/user/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['username'], 'testuser')

if __name__ == '__main__':
    unittest.main()
