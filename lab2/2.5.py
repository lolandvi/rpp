# Задание 2. Работа со строками в Python (вариант №5).
input_str = input("Введите произвольную строку: ")
result_str = ""

for x in input_str:
    if "A" <= x <= "Z" or "А" <= x <= "Я":
        result_str += chr(ord(x) + 32)
    else:
        result_str += x

print("Результат замены всех заглавных букв на строчные:")
print(result_str)

