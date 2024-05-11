import random
import string


def generate_password():
    characters_ask = input("How many characters you want ? (15 by default) : ")
    lowercase_ask = input("You want lower letters ? ('y' by default) : (y/n) ").lower()
    uppercase_ask = input("You want upper letters ? : (y/n) ('y' by default) ").lower()
    special_characters_ask = input("You want special characters ? : (y/n) ('y' by default) ").lower()
    numbers_ask = input("You want numbers ? : (y/n) ('y' by default) ").lower()

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_characters = string.punctuation
    numbers = string.digits

    if characters_ask == "":
        characters_ask = 15
    else:
        characters_ask = int(characters_ask)

    personal_password = ''

    if lowercase_ask == "y":
        personal_password += lowercase
    if uppercase_ask == "y":
        personal_password += uppercase
    if special_characters_ask == "y":
        personal_password += special_characters
    if numbers_ask == "y":
        personal_password += numbers

    if not personal_password:
        print("You must choose at least one category of characters.")
        return None

    password = ''.join(random.choice(personal_password) for _ in range(characters_ask))
    return password
