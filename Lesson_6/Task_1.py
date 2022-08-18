"""4. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
from random import randint
from sys import getsizeof


first_arr = [randint(0, 100) for i in range(10) ] #массив в котором будем искать
print(' Было   ', first_arr)
min_ = min(first_arr)
max_ = max(first_arr)
index_max = first_arr.index(max_)
index_min = first_arr.index(min_)
first_arr[index_max], first_arr[index_min] = first_arr[index_min], first_arr[index_max]
print(' Стало  ', first_arr)

list_of_vars = (min_, max_, index_min, index_max)


result = 0
for i in list_of_vars:
    result += getsizeof(i) + getsizeof(first_arr)

print(f' Задействовано {result} байт пам"яти ')

"""4. Определить, какое число в массиве встречается чаще всего."""
from collections import Counter
from random import randint
first_arr = [randint(0, 100) for i in range(24) ] #изменил размер массива чтобы был такой же как в первом скрипте
a = Counter(first_arr).most_common(1)
#b = 0
second_result = getsizeof(first_arr) + getsizeof(a)# + getsizeof(b)
print(f' Чаще всего встречаеться число {a} раза \n Задействовано {second_result} байт памяти')

# во второй програме памяти задействовано меньше 848 против 248. В принципе логично , поскольку переменных там тоже меньше
# если поиграться с размером массива получаетсья интересно - от 10 до 16 обьектов выдают все те же 248 байт. А 17-24 - уже 312 байт
# но переменные занимают больше места