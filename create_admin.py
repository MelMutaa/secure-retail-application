# Create a new admin here (Pre-prod/dev)
import json
from flask_bcrypt import Bcrypt

def create_admin_user():
    # Initialize Bcrypt
    bcrypt = Bcrypt()
    
    # Get admin username and plaintext password from user input
    username = input("Enter admin username: ")
    plaintext_password = input("Enter admin password: ")
    
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')
    
    # Create user object
    user = {
        username: {
            'password': hashed_password,
            'is_admin': True
        }
    }
    
    # Load existing users
    try:
        with open("data/users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    
    # Add new admin user
    users.update(user)
    
    # Save updated users back to JSON file
    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=4)

    print(f"Admin user '{username}' created successfully!" )

if __name__ == "__main__":
    create_admin_user()
