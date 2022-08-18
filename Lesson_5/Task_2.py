"""Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F
. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
 произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
from collections import deque
a = input('Введите первое число ').upper() #строка это тоже массив
b = input('Введите второе число ').upper()
first_num = [i for i in a]
second_num = [i for i in b]
a = int(a, 16)
b = int(b, 16)
c = 0
result = deque()

def sum(a, b):
    c = a + b
    return c

def multi(a,b):
    c = a * b
    return c

oper = input('ВВедите "+" если нужна операция сложения  \n"*" если нужна операция сложения')
if oper == "+":
    c = (hex(sum(a, b))).upper()
    c = c[2:]
    result = [i for i in c]  # чтобы ответ был как в условии задачи
    print(f'Результат операции сложения для чисел {first_num} и {second_num} равен {result} ')
if oper == "*":
    c = (hex(multi(a, b))).upper()
    c = c[2:]
    result = [i for i in c]
    print(f'Результат операции умножения для чисел {first_num} и {second_num} равен {result} ')
