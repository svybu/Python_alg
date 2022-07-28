"""Найти максимальный элемент среди минимальных элементов столбцов матрицы"""
import random

matrix = []
list_min = []

for i in range(5):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for j in range(5)])

list_min.extend(matrix[0])

for k in matrix:
    print()
    print(('{:4d} ' * len(k)).format(*k))
    i = 0
    for l in k:
        if l < list_min[i]:
            list_min[i] = l
        i += 1

print(('{:4d} ' * len(list_min)).format(*list_min))


list_min.sort(reverse=True)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {list_min[0]}')