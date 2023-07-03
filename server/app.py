#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('Python Operations with Flask Routing Views.')
    return '<h1>Python Operations with Flask Routing Views.</h1>'

@app.route('/print/<string:username>')
def print_string(username):
    print(username)
    return f'Hello {username}'

@app.route('/count/<int:number>')
def count(number):
    count = 0
    for n in range(number):
        count += n
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
