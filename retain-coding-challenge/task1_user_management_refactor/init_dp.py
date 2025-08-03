# Dummy DB initializer
from models import users

def init_db():
    users.clear()
    users.extend([
        {"id": 1, "name": "Alice", "email": "alice@example.com", "password": "alice123"},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "password": "bob123"},
    ])
    print("Database initialized with dummy users.")

if __name__ == '__main__':
    init_db()
