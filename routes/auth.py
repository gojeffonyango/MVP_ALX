from flask import Blueprint, request
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return AuthService.register(data['username'], data['password'], data['email'])

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return AuthService.login(data['username'], data['password'])

