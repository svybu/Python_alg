""" Среди натуральных чисел, которые были введены, найти наибольшее по сумме
 цифр. Вывести на экран это число и сумму его цифр."""

max_num = 0
max_sum = 0
def calc_2(number):
    sum = 0
    for h in number:
        sum += int(h)
    return sum

str_num = [i for i in input('Введите последовательность натуральных чисел через пробел').split(' ')]

for j in str_num:
    if calc_2(j) > max_sum:
        max_num = j
        max_sum = calc_2(j)

print(f'в {max_num} сума цифр {max_sum}')

