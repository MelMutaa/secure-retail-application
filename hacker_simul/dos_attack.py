# Simulate DoS attack by overloading the system with login requests

import time
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from security_manager import SecurityManager

def simulate_dos_attack():
    """Simulate a Denial of Service (DoS) attack by flooding the system with login requests."""
    security_manager = SecurityManager()
    username = "admin"  
    password = "incorrect_password"  

    try:
        for i in range(100000):  
            print(f"Attempt {i+1}: Sending login request...")
            security_manager.authenticate(username, password)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("DoS attack simulation interrupted by user.")

if __name__ == "__main__":
    simulate_dos_attack()
