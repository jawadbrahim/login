from .blueprints import login_bp
from flask import Blueprint
from .controller import create_login
login_bp=Blueprint('/login',__name__,url_prefix='/login')

@login_bp.route('/',methods=["POST"],strict_slashes=False)
def login():
    return create_login()