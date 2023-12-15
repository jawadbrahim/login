from flask import request, jsonify
from database.postgres import sqlalchemy_db
from .exception import LOGIN_SUCEFFULY, EMAIL_NOT_FOUND, INVALID_PASSWORD

from project.model.login import Login
from project.model.user import User
from .helpers.hashing import HashingHelper

hash_helper = HashingHelper()

def create_login():
    if request.method == "POST":
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        hashed_password = hash_helper.sha256(password)

        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            return jsonify(EMAIL_NOT_FOUND)

        stored_hashed_password = existing_user.password

        if stored_hashed_password and hashed_password == stored_hashed_password:
    
            login_data = Login(email=email, password=hashed_password)
            sqlalchemy_db.session.add(login_data)
            sqlalchemy_db.session.commit()

            return jsonify(LOGIN_SUCEFFULY)
        else:
            return jsonify(INVALID_PASSWORD)
