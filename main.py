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

def format_text(text_number):
    text_index = int(text_number) - 1
    text = TEXTS[text_index].replace(". ", " ").replace(", ", " ").replace("-", " ").replace("\n", " ").strip().split(" ")
    return text

def count_words(text_number):
    text = format_text(text_number)
    return len(text)

def occurences(n):
    text = format_text(text_number)
    number_of_occurences = {}
    for word in text:
        if not len(word) in number_of_occurences:
            number_of_occurences[len(word)] = [word]
        else:
            number_of_occurences[len(word)].append(word)
    return sorted(number_of_occurences.items())

def count_titlecase_words(text_number):
    text = format_text(text_number)
    titlecase_words = []
    for word in text:
        if word.istitle():
            titlecase_words.append(word)
    return len(titlecase_words)

def count_uppercase_words(text_number):
    text = format_text(text_number)
    uppercase_words = []
    for word in text:
        if word.isupper() and word.isalpha():
            uppercase_words.append(word)
    return len(uppercase_words)

def count_lowercase_words(text_number):
    text = format_text(text_number)
    lowercase_words = []
    for word in text:
        if word.islower():
            lowercase_words.append(word)
    return len(lowercase_words)

def count_and_sum_numeric_strings(text_number):
    text = format_text(text_number)
    numeric_strings = []
    for word in text:
        if word.isnumeric():
            numeric_strings.append(int(word))
    return len(numeric_strings), sum(numeric_strings)


def main(text_number):
    print(f"There are {count_words(text_number)} words in the selected text.")
    print(f"There are {count_titlecase_words(text_number)} titlecase words.")
    print(f"There are {count_uppercase_words(text_number)} uppercase words.")
    print(f"There are {count_lowercase_words(text_number)} lowercase words.")
    print(f"There are {count_and_sum_numeric_strings(text_number)[0]} numeric strings.")
    print(f"The sum of all the numbers {count_and_sum_numeric_strings(text_number)[1]}.")
    print(occurences(text_number))    
    
if username in registered_users.keys() and password in registered_users[username]:
    print(separator)
    print(f"Welcome to the app, {username} {new_line}We have 3 text to be analyzed.")
    print(separator)
    text_number = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)
    if not text_number.isdigit() or int(text_number) > 3 or int(text_number) <= 0:
        print("given input is not correct, terminating the program...")
        exit()
    else:
        main(text_number)
else:
    print("unregistered user, terminating the program...")
    exit()