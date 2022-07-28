"""В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

from random import randint
first_arr = []
first_arr = [randint(-100, 100) for i in range(20)]  #массив в котором будем искать
print(first_arr)
a = min(first_arr)
first_arr.remove(a)
b = min(first_arr)
print(f'Минимальные значения массива - {a} и {b}')