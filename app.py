from flask import Flask, request, jsonify
import random

app = Flask(__name__)

operations = ['Умножение', 'Сложение', 'Вычитание', 'Деление']

@app.route('/number/', methods=['GET'])
def get_number():
    param = int(request.args.get('param', 0))
    random_number = random.randint(1, 10)
    operation = random.choice(operations)

    if operation == 'Умножение':
        result = random_number * param
    elif operation == 'Сложение':
        result = random_number + param
    elif operation == 'Вычитание':
        result = random_number - param
    elif operation == 'Деление':
        result = random_number / param if param != 0 else 0

    response = {
        'Результат': result,
        'Операция': operation
    }

    return jsonify(response)

@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()

    if 'jsonParam' not in data:
        return jsonify({'error': 'Missing jsonParam field in request'}), 400

    json_param = data['jsonParam']
    random_number = random.randint(1, 10)
    operation = random.choice(operations)

    if operation == 'Умножение':
        result = random_number * json_param
    elif operation == 'Сложение':
        result = random_number + json_param
    elif operation == 'Вычитание':
        result = random_number - json_param
    elif operation == 'Деление':
        result = random_number / json_param if json_param != 0 else 0

    response = {
        'Результат': result,
        'Операция': operation
    }

    return jsonify(response)

@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_number = random.randint(1, 10)
    operation = random.choice(operations)

    response = {
        'Число': random_number,
        'Операция': operation
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)