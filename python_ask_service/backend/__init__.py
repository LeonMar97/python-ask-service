from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
# from python_ask_service.backend.models import Question
# Load environment variables from .env file
load_dotenv()


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    '''SQLAlchemy conf'''

    db.init_app(app)
    '''init db, and sholuld create the table automatically from models'''
    with app.app_context():
        db.create_all()
        '''the tables didnt create automatically, so i added this for now'''
    return app
