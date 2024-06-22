import os
#importing the clear function into the main.py file
def clear():
    # For Windows operating systems
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux operating systems
    else:
        os.system('clear')
