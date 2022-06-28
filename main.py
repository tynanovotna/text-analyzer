"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN#4503
"""

import task_template

separator = "-" * 40
new_line = "\n"
registred_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "lizz": "pass123"
}
username = input("username: ").lower()
password = input("password: ").lower()
if username in registred_users.keys() and password in registred_users[username]:
    print(separator)
    print(f"Welcome to the app, {username} {new_line}We have 3 text to be analyzed.")
    print(separator)
else:
    print("unregistered user, terminating the program...")
    exit()