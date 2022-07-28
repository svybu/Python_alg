"""4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;случайное вещественное число;случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""
import random
result = 0
try:
    start, stop =input('ВВедите начало и конец диапазона через пробел ').split()
    if start.isdigit() == True and stop.isdigit() == True :
        a = int(input('ВВедите 1 если генерируем целое число. 2 - если вещественное '))
        if a == 1:
            start = int(start)
            stop = int(stop)
            result = random.randint(start, stop)
        elif a == 2:
            start = float(start)
            stop = float(stop)
            result = random.uniform(start, stop)
    elif start.isalpha() == True and stop.isalpha() == True:
        result = chr(random.randint(ord(start), ord(stop)))
    else:
        print('нужно было ввести или два числа или две буквы')
    print(result)
except:
    print('нужно было ввести или два числа или две буквы ')
