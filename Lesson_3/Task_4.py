"""4. Определить, какое число в массиве встречается чаще всего."""
from collections import Counter
from random import randint
first_arr = [randint(0, 100) for i in range(100) ] #массив в котором будем искать
a = Counter(first_arr).most_common(1)
print(f' Чаще всего встречаеться число {a} раза')
