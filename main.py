"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN#4503
"""

from task_template import TEXTS

SEPARATOR = "-" * 40

def format_text(text_number):
    text_index = int(text_number) - 1
    text = TEXTS[text_index].replace(". ", " ").replace(", ", " ").replace("-", " ").replace("\n", " ").strip().split(" ")
    return text

def count_words(text_number):
    text = format_text(text_number)
    return len(text)

def occurences(text_number):
    text = format_text(text_number)
    number_of_occurences = {}
    for word in text:
        if not len(word) in number_of_occurences:
            number_of_occurences[len(word)] = [word]
        else:
            number_of_occurences[len(word)].append(word)
    return sorted(number_of_occurences.items())

def analyze_text(text_number):
    text = format_text(text_number)
    titlecase_words = []
    uppercase_words = []
    lowercase_words = []
    for word in text:
        if word.istitle():
            titlecase_words.append(word)
        elif word.isupper() and word.isalpha():
            uppercase_words.append(word)
        elif word.islower():
            lowercase_words.append(word)
    return len(titlecase_words), len(uppercase_words), len(lowercase_words)

def count_and_sum_numeric_strings(text_number):
    text = format_text(text_number)
    numeric_strings = []
    for word in text:
        if word.isnumeric():
            numeric_strings.append(int(word))
    return len(numeric_strings), sum(numeric_strings)

def make_chart(text_number):
    chart_data = occurences(text_number)
    print(SEPARATOR)
    max_len_value = 0
    for _, value in chart_data:
        if len(value) > max_len_value:
            max_len_value = len(value)
    print("LEN", "|", "OCCURENCES".center(max_len_value), "|", "NR." )
    print(SEPARATOR)
    for key, value in chart_data:
        print(str(key).rjust(3), "|", len(value) * "*", "|".rjust(max_len_value + 1 - len(value)), len(value))
    print(SEPARATOR)

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "lizz": "pass123"
    }
username = input("username: ").lower()
password = input("password: ").lower()
    
if username in registered_users.keys() and password in registered_users[username]:
    print(SEPARATOR)
    print(f"Welcome to the app, {username}\nWe have 3 text to be analyzed.")
    print(SEPARATOR)
    text_number = input("Enter a number btw. 1 and 3 to select: ")
    print(SEPARATOR)
    if not text_number.isdigit() or int(text_number) > 3 or int(text_number) <= 0:
        print("given input is not correct, terminating the program...")
        exit()
    else:
        titlecase_words, uppercase_words, lowercase_words = analyze_text(text_number)
        numeric_strings, sum_numeric_strings = count_and_sum_numeric_strings(text_number)
        print(f"There are {count_words(text_number)} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_strings} numeric strings.")
        print(f"The sum of all the numbers {sum_numeric_strings}.")   
        make_chart(text_number)
else:
    print("unregistered user, terminating the program...")
    exit()