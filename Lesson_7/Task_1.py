"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
 массив, заданный случайными числами на промежутке [-100; 100).
 Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
 реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее)."""
from random import randint
task = [randint(-101,100) for i in range(100)]
print (f'было {task}')
result = []
#print(len(task))

def bubble(task):
    n = 1
    while n < len(task):
        for i in range(len(task)-n):
            if task[i] < task[i+1]:
                task[i], task[i+1]= task[i+1], task[i]
        n += 1
    return f'стало {task}'

print(bubble(task))

