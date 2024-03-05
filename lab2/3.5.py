import sys

# 1. Считываем одномерный массив из параметров командной строки
vhod = [int(x) for x in sys.argv[1:]]

# 2. Выводим пары отрицательных чисел, стоящих рядом
otric = [(vhod[i], vhod[i+1]) for i in range(len(vhod)-1) if vhod[i] < 0 and vhod[i+1] < 0]
print("Пары отрицательных чисел, стоящих рядом:")
print(otric)

# 3. Удаляем все одинаковые повторяющиеся числа
unique = list(set(vhod))

# 4. Выводим полученный массив
print("Полученный массив:")
print(unique)

