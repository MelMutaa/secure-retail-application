import sys
import os
import pytest
import json

# Insert the parent directory into the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from security_manager import SecurityManager

# Setup a temporary user file path for testing
test_users_file = os.path.join(os.path.dirname(__file__), "../data/users_test.json")

@pytest.fixture
def security_manager():
    """Fixture for secure authentication using bcrypt-hashed passwords."""
    # Ensure the directory for the test users file exists
    test_directory = os.path.dirname(test_users_file)
    if not os.path.exists(test_directory):
        os.makedirs(test_directory, exist_ok=True)

    sm = SecurityManager()
    sm.users_file = test_users_file

    # Add a test user with hashed password (bcrypt)
    test_user = {
        "test_user": {
            "bcrypt": sm.bcrypt.generate_password_hash("correct_password").decode('utf-8'),  
            "is_admin": False
        }
    }

    # Write the test user data to the file
    with open(test_users_file, 'w') as file:
        json.dump(test_user, file, indent=4)
        print(f"Test user written to {test_users_file}")

    # Load the users from the file
    sm.load_users()
    return sm


@pytest.fixture
def security_manager_insecure():
    """Fixture for insecure authentication using plaintext passwords."""
    test_directory = os.path.dirname(test_users_file)
    if not os.path.exists(test_directory):
        os.makedirs(test_directory, exist_ok=True)

    sm = SecurityManager()
    sm.users_file = test_users_file

    # Add a test user with plaintext password
    test_user = {
        "test_user": {
            "password": "correct_password",  # Plaintext password
            "is_admin": False
        }
    }

    # Write the test user data to the file
    with open(test_users_file, 'w') as file:
        json.dump(test_user, file, indent=4)

    # Load the users from the file
    sm.load_users()
    return sm


# Test function for secure authentication (hashed password)
def test_user_authentication_secure(security_manager):
    """Test for secure authentication (bcrypt hashed password)."""
    result = security_manager.authenticate("test_user", "correct_password")
    print(f"Authentication result for 'test_user' (secure): {result}")
    assert result == True


# Test function for insecure authentication (plaintext password)
def test_user_authentication_insecure(security_manager_insecure):
    """Test for insecure authentication (plaintext password)."""
    result = security_manager_insecure.authenticate("test_user", "correct_password")
    print(f"Authentication result for 'test_user' (insecure): {result}")
    assert result == True

