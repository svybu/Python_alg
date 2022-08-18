"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
 на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""
from random import randint
task = [randint(-1,50) for i in range(50)]
print (f'было {task}')
result = []
#print(len(task))

def divide(task):
    if len(task) > 1:
        mid = len(task) // 2
        part_1 = task[:mid]
        part_2 = task[mid:]

        divide(part_1)
        divide(part_2)

        i = 0
        j = 0
        k = 0
        while i < len(part_1) and j < len(part_2):
            if part_1[i] < part_2[j]:
                task[k] = part_1[i]
                i = i + 1
            else:
                task[k] = part_2[j]
                j = j + 1
            k = k + 1

        while i < len(part_1):
            task[k] = part_1[i]
            i = i + 1
            k = k + 1

        while j < len(part_2):
            task[k] = part_2[j]
            j = j + 1
            k = k + 1
    return f'стало {task}'

print(divide(task))