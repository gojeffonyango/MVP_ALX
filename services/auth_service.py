from flask import jsonify
from flask_jwt_extended import create_access_token
from models import mongo, User
import bcrypt

class AuthService:
    @staticmethod
    def register(username, password, email):
        user = mongo.db.users.find_one({"username": username})
        if user:
            return jsonify({"msg": "User already exists"}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username, hashed_password, email)
        mongo.db.users.insert_one(new_user.__dict__)
        return jsonify({"msg": "User registered successfully"}), 201

    @staticmethod
    def login(username, password):
        user = mongo.db.users.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            access_token = create_access_token(identity=user["username"])
            return jsonify(access_token=access_token), 200
        return jsonify({"msg": "Bad username or password"}), 401

