# cmd_injections.py - Simulate command through user input in a CLI
import os


def run_system_command(command):
    # Directly executes user input as a system command (unsafe)
    os.system(command)


# Simulate an injection attempt by a user
user_input = "ls; rm -rf /"  
run_system_command(user_input)
