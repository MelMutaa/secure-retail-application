# user.py - User management functionality

import json
import bcrypt


class UserManager:
    def __init__(self):
        self.users_file = 'data/users.json'
        self.load_users()

    def load_users(self):
        """Load user data from JSON file."""
        try:
            with open(self.users_file, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        """Save user data to JSON file."""
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file, indent=4)

    def add_user(self, username, password, is_admin=False, secure=True):
        """Add a new user to the system.
           Hash the password if secure mode is on."""
        if username in self.users:
            print(f"User {username} already exists.")
            return False

        # If in secure mode, hash the password before storing
        if secure:
            hashed_password = bcrypt.hashpw(password.encode(
                'utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.users[username] = {
                'password': hashed_password,
                'is_admin': is_admin
            }
        else:
            # Store the password in plaintext in insecure mode
            self.users[username] = {
                'password': password,
                'is_admin': is_admin
            }

        self.save_users()
        print(f"User {username} added successfully.")
        return True

    def update_user(self):
        """Update an existing user's information."""
        username = input("Enter the username to update: ")
        if username in self.users:
            new_password = input("Enter new password: ")
            self.users[username]['password'] = bcrypt.hashpw(
                new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.save_users()
            print(f"User {username} updated successfully.")
        else:
            print(f"User {username} not found.")

    def delete_user(self):
        """Delete an existing user from the system."""
        username = input("Enter the username to delete: ")
        if username in self.users:
            del self.users[username]
            self.save_users()
            print(f"User {username} deleted successfully.")
        else:
            print(f"User {username} not found.")

    def change_password(self):
        """Change the password for the logged-in user."""
        username = input("Enter your username: ")
        old_password = input("Enter your old password: ")
        new_password = input("Enter your new password: ")

        if self.authenticate(username, old_password):
            self.users[username]['password'] = bcrypt.hashpw(
                new_password.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8')
            self.save_users()
            print("Password changed successfully.")
        else:
            print("Old password is incorrect.")

    def apply_discount_code(self, code):
        """Apply a discount code (dummy functionality for now)."""
        valid_codes = {"DISCOUNT10", "SAVE20", "HOLIDAY30"}
        return code in valid_codes

    def authenticate(self, username, password):
        """Authenticate a user by checking the password."""
        if username in self.users:
            stored_password = self.users[username]['password']
            if 'bcrypt' in stored_password:
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
            else:
                return stored_password == password  
        return False
