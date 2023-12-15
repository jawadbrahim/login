# project/features/users/routes.py
from flask import Blueprint, jsonify, request
from project.features.users_register.controller import users_register

register_bp = Blueprint('register', __name__,url_prefix="/register")

@register_bp.route("/",methods=["POST"],strict_slashes=False)
def register():
    return users_register()