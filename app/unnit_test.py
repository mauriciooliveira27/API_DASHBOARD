import unittest
from models import DashBoard, db
from flask import Flask
from dotenv import load_dotenv
import os

class TestDashboardModel(unittest.TestCase):
    def setUp(self):
        self.DB_name = 'web_api'
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:7iv7cs5n@localhost/{self.DB_name}'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:7iv7cs5n@localhost/{self.DB_name}'
        db.init_app(self.app)
        # with self.app.app_context():
        #     db.create_all()

    # def tearDown(self):
    #     with self.app.app_context():
    #         db.session.remove()
    #         db.drop_all()

    def test_create_dashboard_entry(self):
        
        with self.app.app_context():
            # Create a Dashboard entry and add it to the test database
            dashboard_entry = DashBoard(tensao=220.0, corrente=10.0, potencia_ativa=2200.0)
            db.session.add(dashboard_entry)
            db.session.commit()

            # Query the database and assert that the entry was added
            queried_entry = DashBoard.query.get(dashboard_entry.id)
            self.assertEqual(queried_entry.tensao, 220.0)
            self.assertEqual(queried_entry.corrente, 10.0)
            self.assertEqual(queried_entry.potencia_ativa, 2200.0)

if __name__ == '__main__':
    unittest.main()