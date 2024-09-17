from flask import Blueprint, jsonify

from app.controllers.user_controller import UserController

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/profile')
def profile():
    return jsonify({"message": "User profile"})

@user_bp.route('/hello-world')
def hello_world():
    return jsonify({"message": UserController().hello() })
@user_bp.route('/settings')
def settings():
    return jsonify({"message": "User settings"})
