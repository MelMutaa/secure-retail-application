"""main.py - Entry to the retail application."""
from datetime import datetime
from secure_api import SecureAPI
from insecure_api import InsecureAPI


def get_greeting():
    """Return a greeting message based on the current time."""
    now = datetime.now()
    hours = now.hour
    if 5 <= hours < 12:
        greeting = "Good Morning!"
    elif 12 <= hours < 17:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    return greeting


def main():
    """Return main function of the retail app."""
    greeting = get_greeting()
    print((greeting), "Welcome to the Secure Retail App CLI...", '\n')
    while True:
        print("Choose an option:")
        print("1. Login to run Secure Mode (Admin only)", '\n')
        print("2. Insecure Mode (Open to all users!)", '\n')
        print("3. Exit the application...", '\n')
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
          SecureAPI().run_secure_mode()
        elif choice == '2':
             InsecureAPI().run_insecure_mode()
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
