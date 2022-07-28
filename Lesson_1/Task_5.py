"""Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв."""
try:
    first, last = input('Введите две буквы латинского алфавита через пробел ').split()
    first = first.lower()
    last = last.lower()
    if len(first) != 1 or len(last) != 1:
        print('нужно было ввести 2 буквы через пробел(')
    else:
        first_num = ord(first) - 96
        last_num = ord(last) - 96
        distance = abs(first_num-last_num) - 1
        print(f'{first_num} - место первой буквы \n'
              f'{last_num} - место второй буквы \n'
              f'{distance} - букв между ними ')
except:
    print('нужно было ввести две буквы через пробел. Попробуйте еще раз')