import requests

# Задание 1: Отправить запрос GET /number с параметром запроса param=[рандомное число от 1 до 10]
response = requests.get('http://127.0.0.1:5000/number?param=5')
data1 = response.json()
print("Ответ на Задание 1:", data1)

# Задание 2: Отправить запрос POST /number с телом JSON {"jsonParam": [рандомное число от 1 до 10]}
response = requests.post('http://127.0.0.1:5000/number', json={'jsonParam': 7}, headers={'Content-Type': 'application/json'})
data2 = response.json()
print("Ответ на Задание 2:", data2)

# Задание 3: Отправить запрос DELETE /number/
response = requests.delete('http://127.0.0.1:5000/number')
data3 = response.json()
print("Ответ на Задание 3:", data3)

# Выполнение операций
result = data1.get('Результат', 0)

if data2.get('Операция') == 'Сложение':
    result += data2.get('Результат', 0)
elif data2.get('Операция') == 'Вычитание':
    result -= data2.get('Результат', 0)
elif data2.get('Операция') == 'Умножение':
    result *= data2.get('Результат', 1)
elif data2.get('Операция') == 'Деление':
    result /= data2.get('Результат', 1)

if data3.get('Операция') == 'Сложение':
    result += data3.get('Число', 0)
elif data3.get('Операция') == 'Вычитание':
    result -= data3.get('Число', 0)
elif data3.get('Операция') == 'Умножение':
    result *= data3.get('Число', 1)
elif data3.get('Операция') == 'Деление':
    result /= data3.get('Число', 1)

print("\nРезультат выражения:", result)