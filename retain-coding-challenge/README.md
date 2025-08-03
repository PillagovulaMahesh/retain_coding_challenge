# 🧠 Retain Coding Challenge

This repository includes solutions for both parts of the Retain coding challenge:

1. **Task 1** – Refactor a legacy User Management API  
2. **Task 2** – Build a simple URL Shortener Service

---


---

## ✅ Task 1: User Management API Refactor

### 📝 Summary

The original user management code was a single messy file. It was refactored into modular components:
- Clear folder and file structure
- Blueprint routing
- In-memory data (no DB dependency)
- RESTful endpoints
- Input validation and basic error handling

### ▶️ Run Instructions


# Move to the task1 folder
cd task1_user_management_refactor

# Install dependencies
pip install -r requirements.txt

# Initialize dummy data
python init_db.py

# Start the app
python app.py
