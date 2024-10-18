
### README for Secure Retail App

---

## Overview
This is a Secure Retail CLI application that allows users to create accounts, browse products, and manage their shopping carts. There are two modes available: **Secure Mode** and **Insecure Mode**. Secure Mode requires admin privileges and stores passwords securely (hashed), while Insecure Mode allows for plaintext password storage. The application includes basic product management, discount codes, and security logging features. 

The system also supports intrusion detection, secure payment storage, and session timeout for enhanced security.

---

## Prerequisites
Before running the application, you need to install the required dependencies. Follow the steps below to set up the application environment.

### 1. **Setting Up the Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
```

### 2. **Install Required Dependencies**
All dependencies are listed in the `requirements.txt` file. To install the required Python libraries, run the following command:

```bash
pip install -r requirements.txt
```

### 3. **Dependencies Included**
- `bcrypt`: For password hashing in secure mode.
- `Flask-Bcrypt`: To securely hash and check passwords.
- `pytest`: For running the test suite.
- `flake8`: For code linting and adhering to PEP 8 guidelines.

---

## Running the Application

### 1. **Starting the Application**
To start the retail application, run the `main.py` file from the root of the project:

```bash
python main.py
```

You will be prompted with options:
- **Secure Mode**: Requires admin login with hashed password.
- **Insecure Mode**: Allows non-admin users to create accounts and login with plaintext passwords.
- **Exit**: Exits the application.

### 2. **Creating an Admin Account (For Secure Mode)**
To create an admin account, enter **Insecure Mode**, create an account, and set the user as an admin:

```bash
# Run main.py and select Insecure Mode
python main.py
# Create account, assign admin privileges
```

Alternatively, in **Secure Mode**, admins can create new admin accounts directly using the admin panel.

### 3. **Browsing Products and Managing Basket**
In **Insecure Mode**, you can:
- View products
- Add and remove items from your basket
- Apply discount codes

To interact with products:
```bash
# Insecure Mode -> User Panel
python main.py
# Follow the prompts to view products, add/remove from the basket, and apply discounts.
```

### 4. **Testing Security Features**
In **Secure Mode**, you have access to:
- **Manage Users**: Create, update, and delete users with secure password hashing.
- **Manage Products**: Add, update, and delete products.
- **View Security Logs**: View all security-related events (successful and failed login attempts, etc.).
- **Store and Retrieve Payment Information**: Securely store and retrieve encrypted payment information for users.

### Command to start secure mode (admin privileges required):
```bash
python main.py
# Login with admin credentials
```

---

## Security Toggle
You can toggle between **Secure Mode** and **Insecure Mode** at the application level.

- **Secure Mode**: Enforces password hashing, logs events, and secures payment information.
- **Insecure Mode**: No password hashing, allows plaintext storage, and has fewer security checks.

Switching between these two modes is simple:
- Secure Mode requires admin login and can be toggled on by selecting the "Login to Secure Mode" option in the CLI.
- Insecure Mode can be selected by any user during the CLI selection process.

---

## Testing

### 1. **Run Test Suite**
The application includes a set of unit tests to validate functionality. You can run the tests using `pytest`:

```bash
pytest tests/
```

### 2. **Running Linter (flake8)**
To ensure the code follows PEP 8 guidelines, you can run `flake8` as a linter:

```bash
flake8 .
```

- Ensure that the output shows no errors or warnings related to style, unused imports, etc.
  
### 3. **Security Tools**
- **Security Logging**: Logs can be found in the `data/security_logs.json` file. This will include login attempts and any security-related actions.
- **Brute Force Detection**: After 3 failed login attempts, the account will be locked for a set period. Test this by entering incorrect passwords multiple times in a row.

---

## Example CLI Interaction

```plaintext
Welcome to the Secure Retail App CLI...

Choose an option:
1. Login to Secure Mode (Admin only)
2. Insecure Mode (Open to all users! | Choose here to create an account or login!)
3. Exit the application...

# Insecure Mode
Enter your choice (1/2/3): 2

Running in Insecure Mode...
1. Login
2. Create an Account
3. Exit
Enter your choice (1/2/3): 2

Enter username: user1
Enter password: password123
Is this user an admin? (yes/no): no
User user1 added successfully.

# Secure Mode (Admin Only)
Enter your choice (1/2/3): 1

[Admin Login Required for Secure Mode]
Enter admin username: admin_user
Enter admin password: [password hashed]

Welcome, admin_user! You have admin access.
```

---

## Additional Information
- All user data is stored in `data/users.json`.
- Products are stored in `data/products.json`.
- Discount codes are checked within the app but can be configured in the code.
