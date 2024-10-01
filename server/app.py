#!/usr/bin/env python3

from flask import Flask, Response  # Ensure Response is imported

app = Flask(__name__)

# Base route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

# Count route
@app.route('/count/<int:number>')
def count(number):
    result = '\n'.join(str(i) for i in range(number + 1))  # Generates numbers from 0 to 'number'
    return Response(result, mimetype='text/plain')

# Math operations route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')  # Ensure num1 and num2 are integers
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation!', 400  # Return error for invalid operations
    return f'<p>{num1} {operation} {num2} = {result}</p>'

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
