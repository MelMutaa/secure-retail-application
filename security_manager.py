# Security manager functionality
# For authentication, authorisation, encryption, and event monitoring.

import os
import json
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt


class SecurityManager:
    def __init__(self):
        self.bcrypt = Bcrypt()  # Initialize Bcrypt

        # Construct the paths to the files
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(base_dir, 'data', 'security_logs.json')
        self.users_file = os.path.join(base_dir, 'data', 'users.json')

        self.failed_attempts = {}
        # Minutes before lockout is lifted
        self.lockout_time = 15

        # Ensure the data folder and files exist
        self.ensure_data_files_exist()

        self.load_logs()
        self.load_users()

    def ensure_data_files_exist(self):
        """Ensure that the data folder and security logs file exist."""
        # Create the data folder if it doesn't exist
        data_folder = os.path.join(os.path.dirname(self.log_file))
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        # Create an empty security_logs.json file if it doesn't exist
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

        # Create an empty users.json file if it doesn't exist
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump({}, f)

    def load_logs(self):
        """Load security logs from JSON file."""
        with open(self.log_file, 'r') as file:
            self.logs = json.load(file)

    def save_logs(self):
        """Save security logs to JSON file."""
        with open(self.log_file, 'w') as file:
            json.dump(self.logs, file, indent=4)

    def load_users(self):
        """Load users from JSON file."""
        with open(self.users_file, 'r') as f:
            self.users = json.load(f)


    def authenticate(self, username, password, admin=False):
        """Authenticate users (hashed for secure, plaintext for insecure)."""
        if self.is_locked_out(username):
            print(f"User {username} is locked out.")
            return False

        user = self.users.get(username)

        if user and 'bcrypt' in user and self.bcrypt.check_password_hash(
                user['bcrypt'], password):
            if admin and not user.get('is_admin', False):
                self.log_event(username, "Failed admin login attempt.")
                return False
            self.log_event(username, "Successful login.")
            self.reset_failed_attempts(username)
            return True
        # Check plaintext password for insecure users
        elif user and user['password'] == password:
            if admin and not user.get('is_admin', False):
                self.log_event(username, "Failed admin login attempt.")
                return False
            self.log_event(username, "Successful login.")
            self.reset_failed_attempts(username)
            return True
        else:
            self.log_event(username, "Failed login attempt.")
            self.increment_failed_attempts(username)
            return False

    def is_locked_out(self, username):
        """Check if the user is locked out due to failed login attempts."""
        if username in self.failed_attempts:
            attempts, last_attempt = self.failed_attempts[username]
            lockout_until = last_attempt + timedelta(minutes=self.lockout_time)

            if attempts >= 3 and datetime.now() < lockout_until:
                return True
            # Reset after lockout period
            elif datetime.now() >= lockout_until:
                self.reset_failed_attempts(username)
        return False

    def increment_failed_attempts(self, username):
        """Track failed login attempts."""
        if username in self.failed_attempts:
            attempts, last_attempt = self.failed_attempts[username]
            self.failed_attempts[username] = (attempts + 1, datetime.now())
        else:
            self.failed_attempts[username] = (1, datetime.now())

        if self.failed_attempts[username][0] >= 3:
            print(f"User {username} is locked out.")

    def reset_failed_attempts(
            self, username):
        """Reset failed login attempts
        after a successful login or lockout period."""
        if username in self.failed_attempts:
            del self.failed_attempts[username]

    def log_event(self, username, event):
        """Log events such as login attempts and other actions."""
        log_entry = {
            'username': username,
            'event': event,
            'timestamp': datetime.now().isoformat()
        }
        self.logs.append(log_entry)
        self.save_logs()

    def store_payment_info(
            self, username, card_number):
        """Encrypt and store payment
        information securely."""
        encrypted_card = self.bcrypt.generate_password_hash(
            card_number).decode('utf-8')
        if username in self.users:
            self.users[username]['payment_info'] = encrypted_card
        self.save_users()
        self.log_event(username, "Stored payment information securely.")

    def load_payment_info(self, username):
        """Retrieve and decrypt payment information."""
        if username in self.users and 'payment_info' in self.users[username]:
            encrypted_card = self.users[username]['payment_info']
            return encrypted_card
        return None

    def save_users(self):
        """Save user data (including encrypted payment information)."""
        with open("data/users.json", "w") as f:
            json.dump(self.users, f, indent=4)

    def view_logs(self):
        """View security logs (admin only)."""
        if not self.logs:
            print("No logs found.")
        else:
            print(
                "Security Logs:")
            for log in self.logs:
                print(
                    f"User: {log['username']} - Event: {log['event']} - Timestamp: {log['timestamp']}")
