"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""

from random import randint
first_arr = [randint(-100, 100) for i in range(50) ] #массив в котором будем искать
print(first_arr)
min = first_arr[0]
for i in first_arr:
    if i < min:
        min = i
if min > 0 or min == 0:
    print(' В массиве нет отрицательных элементов')
else:
    index_min = first_arr.index(min)
print(f' Максимальный отрицательный элемент это {min}. Он находиться на {index_min+1} позиции')