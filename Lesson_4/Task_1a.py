"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
15, 6, 4, 2,  то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с
нуля), т.к. именно в этих позициях первого массива стоят четные числа."""
import timeit
def hw_1a():
    first_arr = [8, 3, 15, 6, 4, 2]
    second_arr = [first_arr.index(i) for i in first_arr if i % 2 == 0]
    #print(second_arr)

def hw_1b():
    first_arr = [8, 3, 15, 6, 4, 2]
    second_arr = []
    for i in first_arr:
        if i % 2 == 0:
            second_arr.append(first_arr.index(i))
    #print(first_arr)
    #print('Индексы четных элементов: ', second_arr)

#hw_1a()
#hw_1b()
print(f"это первый вариант {timeit.timeit('hw_1a()', setup='from __main__ import hw_1a')}")
print(f"это второй вариант {timeit.timeit('hw_1a()', setup='from __main__ import hw_1a')}")
# у меня получаеться что первый вариант работает чуть-чуть медленнее. Возможно использование генератора более ресурснозатратно