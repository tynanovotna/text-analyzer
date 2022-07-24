"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN#4503
"""

from task_template import TEXTS

separator = "-" * 40
new_line = "\n"
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "lizz": "pass123"
    }

username = input("username: ").lower()
password = input("password: ").lower()

def analyze_text(n):
    """ Function for analyzing default texts according user's input. """
    index_of_text = int(number_of_text) - 1
    for word in TEXTS[index_of_text]:
        pass

if username in registered_users.keys() and password in registered_users[username]:
    print(separator)
    print(f"Welcome to the app, {username} {new_line}We have 3 text to be analyzed.")
    print(separator)
    number_of_text = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)
    if not number_of_text.isdigit() or int(number_of_text) > 3 or int(number_of_text) <= 0:
        print("given input is not correct, terminating the program...")
        exit()
    else:
        pass
else:
    print("unregistered user, terminating the program...")
    exit()
print(analyze_text(1))