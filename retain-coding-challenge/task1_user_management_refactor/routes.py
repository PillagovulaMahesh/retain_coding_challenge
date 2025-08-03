from flask import Blueprint, jsonify, request
from models import users
from utils import find_user_by_id, validate_user_data

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def health():
    return jsonify({"status": "OK"}), 200

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({"error": "Invalid user data"}), 400
    new_id = max([u["id"] for u in users], default=0) + 1
    new_user = {"id": new_id, **data}
    users.append(new_user)
    return jsonify(new_user), 201

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({"error": "Invalid user data"}), 400
    user.update(data)
    return jsonify(user), 200

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users.remove(user)
    return jsonify({"message": "User deleted"}), 200

@user_bp.route('/search')
def search_users():
    name = request.args.get("name", "").lower()
    results = [u for u in users if name in u["name"].lower()]
    return jsonify(results), 200

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401
