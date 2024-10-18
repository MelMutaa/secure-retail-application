# insecure_api.py - Insecure API with user login and shopping functionality

from user import UserManager
from product import ProductManager
from security_manager import SecurityManager


class InsecureAPI:
    def __init__(self):
        self.user_manager = UserManager()
        self.product_manager = ProductManager()
        self.security_manager = SecurityManager()

    def run_insecure_mode(self):
        """Run the retail app in insecure mode."""
        print("Running in Insecure Mode...")
        print("1. Login")
        print("2. Create an Account")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            self.login()
        elif choice == '2':
            self.create_account()
        elif choice == '3':
            print("Exiting Insecure Mode...")
            exit()
        else:
            print("Invalid choice.")
            self.run_insecure_mode()

    def login(self):
        """Login without hashed password verification."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.security_manager.authenticate(username, password):
            print(f"Welcome, {username}!")
            self.user_panel()
        else:
            print("Login failed. Invalid username or password.")

    def create_account(self):
        """Create an account without hashing the password (insecure mode)."""
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        is_admin = input("Is this user an admin? (yes/no): "
                         ).lower() == 'yes'
        self.user_manager.add_user(
            username, password, is_admin, secure=False)

    def user_panel(self):
        """User panel with shopping functionality."""
        while True:
            print("\nUser Panel:")
            print("1. View Products")
            print("2. Add Product to Basket")
            print("3. Remove Product from Basket")
            print("4. Apply Discount Code")
            print("5. Change Password")
            print("6. Logout")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.product_manager.view_products()
            elif choice == '2':
                self.product_manager.add_to_basket()
            elif choice == '3':
                self.product_manager.remove_from_basket()
            elif choice == '4':
                self.apply_discount()
            elif choice == '5':
                self.user_manager.change_password()
            elif choice == '6':
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

    def apply_discount(self):
        """Apply a discount code."""
        code = input("Enter discount code: ")
        if self.user_manager.apply_discount_code(code):
            print("Discount applied!")
        else:
            print("Invalid discount code.")
