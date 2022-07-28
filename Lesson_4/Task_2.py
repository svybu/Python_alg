"""Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»"""
import timeit
def with_er(n):
    #sieve = [i for i in range(1, 1000000000)]#не змог реализовать генерацию чисел до i-го по счёту для данного алгоритма, поэтому ограничил диапазон

    sieve = [i for i in range(1, 10000000) if i % 2 != 0]
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0

    return f'{n}-е по счёту простое число {sieve[n]}'



def without_er(i):
    list = [2]
    number = 3
    while len(list) < i:
        flag = True
        for j in list.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            list.append(number)
        number += 1
    return f'{i}-е по счёту простое число {list[-1]}'

a = (with_er(5))
b = (without_er(5))
print(f"это c решетом  {timeit.timeit('a', setup='from __main__ import a')}")
print(f"это без {timeit.timeit('b', setup='from __main__ import b')}")
#у меня с решетом получаееться на 1 милисекунду быстрей
