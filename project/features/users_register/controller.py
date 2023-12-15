# project/features/users/controller.py
from flask import jsonify,request,json

from project.model.user import User
from database.postgres import sqlalchemy_db
from .exception import REGISTER_SUCCEFULY,Email_ALREADY_EXIST
from .helpers.hashing import HashHelper
hash_helper=HashHelper()

def users_register():
    if request.method == "POST":
        data=request.get_json()
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        password=data.get('password')
        hashed_password = hash_helper.sha256(password)
        status=data.get('status')
        create_at=data.get('create_at')
        if User.query.filter_by(email=email).first():
            return jsonify(Email_ALREADY_EXIST)
        new_user=User(first_name=first_name,
                          last_name=last_name,
                          email=email,
                      password=hashed_password,
                      status=status,
                      create_at=create_at)
        sqlalchemy_db.session.add(new_user)
        sqlalchemy_db.session.commit()    
        









    return jsonify(REGISTER_SUCCEFULY)   