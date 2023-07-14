import os

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def upload_file():
    text = request.form['text_input'].replace('\r\n', ' ').split()
    lists_of_unique_symbol = get_unique_symbol_string(text)
    return get_unique_symbol(lists_of_unique_symbol)


def get_unique_symbol_string(user_input):
    lists_of_unique_symbol = []
    for string in user_input:
        for symbol in string:
            if symbol.isalpha() and list(string).count(symbol) == 1:
                lists_of_unique_symbol.append(symbol)
                break
    return lists_of_unique_symbol


def get_unique_symbol(lists_of_symbol):
    for each in lists_of_symbol:
        if lists_of_symbol.count(each) == 1:
            return f'unique: {each}'


if __name__ == '__main__':
    app.run(port=os.getenv("APP_PORT", 80), host='0.0.0.0')


