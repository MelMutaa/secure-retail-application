import pytest
import sys
import os

# Insert the parent directory into the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user import UserManager

"""Setup a temporary user file path for testing
(in case user_manager uses users.json)"""
test_users_file = os.path.join(os.path.dirname(__file__), "../data/users_test.json")


@pytest.fixture
def user_manager():
    """Fixture to set up the UserManager with a test users file."""
    um = UserManager()
    # Use the test users file
    um.users_file = test_users_file
    # Reload users from the test file
    um.load_users()  
    return um

def test_add_user(user_manager):
    """Test adding a new user."""
    result = user_manager.add_user("new_user", "password123", secure=True)
    assert result
    assert "new_user" in user_manager.users

def test_delete_user(user_manager, monkeypatch):
    """Test deleting a user with mocked input."""
    # Add a user first
    user_manager.add_user("delete_user", "password123", secure=True)
    
    # Use monkeypatch to mock input() to return "delete_user"
    monkeypatch.setattr('builtins.input', lambda _: "delete_user")
    
    # Call the delete_user() method, which will now use the mocked input
    user_manager.delete_user()
    
    # Verify that the user was deleted
    assert "delete_user" not in user_manager.users

@pytest.fixture(autouse=True)
def cleanup_users():
    """Clean up the test users file after each test."""
    yield
    if os.path.exists(test_users_file):
        os.remove(test_users_file)