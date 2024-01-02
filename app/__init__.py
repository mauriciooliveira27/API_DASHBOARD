from flask import Flask
from dotenv import load_dotenv
import os
from .models import DashBoard, db


class ApiApplication:

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.DB_name = 'teste'

    
    def app_configure(self):
        
        load_dotenv()

        self.app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:7iv7cs5n@localhost/{self.DB_name}'
        db.init_app(self.app)
        # with self.app.app_context():
        #     db.create_all()
    
    
    def initialization(self):
        self.app_configure()

        
    def run(self, debug):
        self.initialization()
        self.app.run(debug=debug)