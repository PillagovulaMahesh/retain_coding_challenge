from models import users

def find_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)

def validate_user_data(data):
    if not isinstance(data, dict):
        return False
    required = {"name", "email", "password"}
    return required.issubset(data.keys())
