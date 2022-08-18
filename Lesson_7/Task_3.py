"""Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
 в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
  то используйте метод сортировки, который не рассматривался на уроках"""
import random
def median(arr, k ):
    centre = random.choice(arr)
    left_part =[i for i in arr if i < centre]
    right_part = [i for i in arr if i > centre]
    centers = [i for i in arr if i == centre]
    if k < len(left_part):
        return median(left_part, k)
    elif k < len(left_part) + len(centers):
        return centers[0]
    else:
        return median(right_part, k - len(left_part)-len(centers))

m = 20
arr = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f' было {arr}\n медиана {median(arr, len(arr)/2)}')
