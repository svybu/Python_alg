"""Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""

matrix = []

for i in range(4):
    matrix.append([])
    sum = 0
    for j in range(4):
        elem = int(input(f'Введите элемент {i+1} строки и {j+1} столбца  '))
        sum += elem
        matrix[i].append(elem)
    matrix[i].append(sum)
#print(matrix)
for k in matrix:
    print(('{:>4d}' * 5).format(*k))