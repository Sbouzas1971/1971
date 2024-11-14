import os
import sys
import time

from your_mac import TheOracle

def get_command():
    """Gets a command from the user."""
    command = input("Enter your command: ")
    return command

def process_command(command):
    """Processes the command."""
    response = oracle.process_natural_language(command)
    return response

oracle = TheOracle()

while True:
    command = get_command()
    response = process_command(command)
    print(response)