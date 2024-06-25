from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(minlength, include_numbers=True, include_symbols=True):
    alphabet = string.ascii_letters
    numerical_value = string.digits
    special_symbols = string.punctuation

    valid_chars = alphabet
    if include_numbers:
        valid_chars += numerical_value
    if include_symbols:
        valid_chars += special_symbols

    password = ""
    has_number = False
    has_symbol = False

    while len(password) < minlength or (include_numbers and not has_number) or (include_symbols and not has_symbol):
        new_char = random.choice(valid_chars)
        password += new_char

        if new_char in numerical_value:
            has_number = True
        elif new_char in special_symbols:
            has_symbol = True

    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        minlength = int(request.form['minlength'])
        include_numbers = 'numbers' in request.form
        include_symbols = 'symbols' in request.form

        password = generate_password(minlength, include_numbers, include_symbols)
        return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
