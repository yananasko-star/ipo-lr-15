from app import app
from flask import request

@app.route('/')
def index():
    return 'Привет! Это главная страница.'

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@app.route('/square/<int:number>')
def square(number):
    result = number * number
    return f'Квадрат числа {number} равен {result}.'
