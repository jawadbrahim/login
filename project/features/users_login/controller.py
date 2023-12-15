from flask import request, jsonify
from database.postgres import sqlalchemy_db
from .exception import LOGIN_SUCEFFULY, EMAIL_NOT_FOUND,INVALID_PASSWORD

from project.model.login import Login
from project.model.user import User

def create_login():
    if request.method == "POST":
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

       
        if not User.query.filter_by(email=email).first():
            return jsonify(EMAIL_NOT_FOUND)

        login_user = Login.query.filter_by(email=email, password=password).first()

        if login_user:
            
            return jsonify(LOGIN_SUCEFFULY)
        else:
        
            return jsonify(INVALID_PASSWORD)

    
