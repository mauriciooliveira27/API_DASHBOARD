from flask import Flask
from dotenv import load_dotenv
import os
from .models import DashBoard, db
from .urls import urls

class ApiApplication:

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.DB_name = 'web_api'

    
    def configure_app(self):

        load_dotenv()
        self.app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:7iv7cs5n@localhost/{self.DB_name}'
        self.app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True}

 
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db.init_app(self.app)
        # with self.app.app_context():
        #     db.create_all()
    

    def register_blueprints(self):
        self.app.register_blueprint(urls, url_prefix = '/api')


    def initialization(self):
        self.configure_app()
        self.register_blueprints()

    def run(self, debug):
        self.initialization()
        self.app.run(debug=debug)