from flask import Flask, request, jsonify

app = Flask(name)

# Задание 1: Калькулятор
@app.route('/calc', methods=['GET'])
def calculate():
    # Получаем параметры из строки запроса
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    op = request.args.get('op')

    # Проверяем, все ли параметры переданы
    if a is None or b is None or op is None:
        return jsonify({'error': 'Необходимы параметры: a, b, op'}), 400

    # Выполняем операцию
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None
    }

    if op not in operations:
        return jsonify({'error': 'Недопустимая операция. Используйте +, -, *, /'}), 400

    try:
        result = operations[op](a, b)
        if result is None:
            return jsonify({'error': 'Деление на ноль'}), 400
        return jsonify({'a': a, 'b': b, 'op': op, 'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Задание 2: Статус сервиса
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        'status': 'running',
        'service': 'Flask App'
    })

if name == 'main':
    app.run(debug=True, port=5001) # Меняем порт, чтобы не конфликтовал с task_1
