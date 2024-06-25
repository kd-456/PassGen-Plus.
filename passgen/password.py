import random

def generate_password(min_length, include_numbers=True, include_symbols=True):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerical_value = "0123456789"
    special = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    allowed_characters = alphabet
    if include_numbers:
        allowed_characters += numerical_value
    if include_symbols:
        allowed_characters += special

    password = ""
    has_number = False
    has_special = False

    while len(password) < min_length or (include_numbers and not has_number) or (include_symbols and not has_special):
        new_char = random.choice(allowed_characters)
        password += new_char

        if include_numbers and new_char in numerical_value:
            has_number = True
        elif include_symbols and new_char in special:
            has_special = True

    return password

# Input handling
min_length = int(input("Enter the minimum length of the password you want: "))
include_numbers = input("Include numbers (y/n)? ").lower() == "y"
include_symbols = input("Include symbols (y/n)? ").lower() == "y"

# Generate password
generated_password = generate_password(min_length, include_numbers, include_symbols)
print("Generated Password:", generated_password)
