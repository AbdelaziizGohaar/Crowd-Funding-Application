import json
import re
from datetime import datetime

# Helper function to load all data
def load_data():
    try:
        with open('database.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'users': [], 'projects': []}

# Helper function to save all data
def save_data(data):
    with open('database.json', 'w') as f:
        json.dump(data, f, indent=2)

def validate_egyptian_phone(phone):
    pattern = r'^01[0125][0-9]{8}$'
    return re.match(pattern, phone) is not None

def register():
    data = load_data()
    users = data['users']
    
    print("\n=== Registration ===")
    user = {
        'id': len(users) + 1,
        'first_name': input("First Name: ").strip(),
        'last_name': input("Last Name: ").strip(),
        'email': input("Email: ").strip().lower(),
        'password': input("Password: "),
        'mobile_phone': '',
        'created_at': datetime.now().isoformat()
    }
    
    if user['password'] != input("Confirm Password: "):
        print("Passwords don't match!")
        return None
    
    while True:
        phone = input("Mobile Phone (Egyptian): ").strip()
        if validate_egyptian_phone(phone):
            user['mobile_phone'] = phone
            break
        print("Invalid Egyptian phone number. Must start with 010, 011, 012, or 015 and be 11 digits.")
    
    if any(u['email'] == user['email'] for u in users):
        print("Email already registered!")
        return None
    
    users.append(user)
    data['users'] = users
    save_data(data)
    print("Registration successful! You can now login.")
    return user

def login():
    data = load_data()
    users = data['users']
    
    print("\n=== Login ===")
    email = input("Email: ").strip().lower()
    password = input("Password: ")
    
    user = next((u for u in users if u['email'] == email), None)
    
    if not user:
        print("User not found. Please register first.")
        return None
    
    if user['password'] != password:
        print("Incorrect password!")
        return None
    
    print(f"Welcome back, {user['first_name']}!")
    return user