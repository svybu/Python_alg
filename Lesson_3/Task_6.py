"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать"""

from random import randint
first_arr = [randint(0, 100) for i in range(10) ] #массив в котором будем искать
second_arr = []
sum = 0
print(' Было   ', first_arr)
min = first_arr[0]
max = first_arr[0]
for i in first_arr:
    if i > max:
        max = i
    elif i < min:
        min = i
index_max = first_arr.index(max)
index_min = first_arr.index(min)
if index_min < index_max:
    second_arr = first_arr[index_min + 1:index_max]
else:
    second_arr = first_arr[index_max + 1:index_min]
for j in second_arr:
    sum += j
print(second_arr)
print(sum)