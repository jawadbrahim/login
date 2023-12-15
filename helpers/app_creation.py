# app_creation.py
from flask import Flask
from dotenv import load_dotenv

import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SECRET_KEY"] = "your_secret_key"
    


    with app.app_context():
        from project.features.users_register.routes import register_bp
        from project.features.users_login.route import login_bp
        app.register_blueprint(register_bp, url_prefix="/register")
        app.register_blueprint(login_bp ,url_prefix='/login')
     
    return app
