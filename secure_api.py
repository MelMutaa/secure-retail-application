# secure_api.py - Secure API with admin functionalities

import getpass
from user import UserManager
from product import ProductManager
from security_manager import SecurityManager


class SecureAPI:
    def __init__(self):
        self.security_manager = SecurityManager()
        self.user_manager = UserManager()
        self.product_manager = ProductManager()

    def run_secure_mode(self):
        """Run secure mode for admin functions."""
        print("Running in Secure Mode...")

        # Admin login process moved to secure API
        self.admin_login()

        while True:
            print("\nAdmin Panel:")
            print("1. Manage Users")
            print("2. Manage Products")
            print("3. View Security Logs")
            print("4. Store Payment Info")
            print("5. Retrieve Payment Info")
            print("6. Exit Secure Mode")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_users()
            elif choice == '2':
                self.manage_products()
            elif choice == '3':
                self.view_logs()
            elif choice == '4':
                self.store_payment_info()
            elif choice == '5':
                self.retrieve_payment_info()
            elif choice == '6':
                print("Exiting Secure Mode...")
                break
            else:
                print("Invalid choice. Try again.")

    def admin_login(self):
        """Prompt the user for admin login and verify credentials."""
        print("\n[Admin Privileges Required for Secure Mode]")
        username = input("Enter admin username: ")
        password = getpass.getpass("Enter admin password: ")

        # Authenticate and verify if the user has admin privileges
        if self.security_manager.authenticate(username, password, admin=True):
            print(f"Welcome, {username}! You have admin access.")
        else:
            print("Access Denied: You must be an admin to access Secure Mode.")
            exit()  

    def manage_users(self):
        """CRUD operations for managing users."""
        print("\nManage Users:")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Back")

        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            is_admin = input(
                "Is this user an admin? (yes/no): "
            ).lower() == 'yes'

            is_secure_user = input(
                "Should this user be secure (hashed password)? (yes/no): "
            ).lower() == 'yes'
            self.user_manager.add_user(
                username,
                password,
                is_admin,
                secure=is_secure_user)
        elif choice == '2':
            self.user_manager.update_user()
        elif choice == '3':
            self.user_manager.delete_user()
        elif choice == '4':
            return
        else:
            print("Invalid choice. Please select again.")

    def manage_products(self):
        """CRUD operations for managing products."""
        print("\nManage Products:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Back")

        choice = input("Enter your choice: ")
        if choice == '1':
            self.product_manager.add_product()
        elif choice == '2':
            self.product_manager.update_product()
        elif choice == '3':
            self.product_manager.delete_product()
        elif choice == '4':
            return
        else:
            print("Invalid choice. Please select again.")

    def view_logs(self):
        """View security logs."""
        self.security_manager.view_logs()

    def store_payment_info(self):
        """Store and encrypt payment info."""
        username = input("Enter username: ")
        card_number = input("Enter credit card number: ")
        self.security_manager.store_payment_info(username, card_number)
        print("Payment information stored securely.")

    def retrieve_payment_info(self):
        """Retrieve encrypted payment info."""
        username = input("Enter username: ")
        payment_info = self.security_manager.load_payment_info(username)
        if payment_info:
            print(f"Encrypted Payment Info for {username}: {payment_info}")
        else:
            print(f"No payment information found for {username}.")

