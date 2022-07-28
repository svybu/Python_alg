"""4. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
from random import randint
first_arr = [randint(0, 100) for i in range(10) ] #массив в котором будем искать
print(' Было   ', first_arr)
min_ = min(first_arr)
max_ = max(first_arr)
index_max = first_arr.index(max_)
index_min = first_arr.index(min_)
first_arr[index_max], first_arr[index_min] = first_arr[index_min], first_arr[index_max]
print(' Стало  ', first_arr)
