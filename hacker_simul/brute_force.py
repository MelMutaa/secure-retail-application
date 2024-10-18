# brute_force.py - Simulate brute force attack

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from security_manager import SecurityManager


def brute_force_attack(username, password_list):
    security_manager = SecurityManager()

    for password in password_list:
        print(f"Trying password: {password}")
        if security_manager.authenticate(username, password):
            print(f"Login successful with password: {password}")
            break
        else:
            print("Login failed. Trying next password...")
        time.sleep(1)


if __name__ == "__main__":
    username = "test7"
    password_list = ["wrongpass1", "wrongpass2",
                     "test7"]  
    brute_force_attack(username, password_list)
