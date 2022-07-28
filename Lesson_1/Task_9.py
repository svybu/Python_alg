try:
    a, b, c = map(int, input('ВВедите три числа через пробел ').split())
    if a < b < c or c < b < a:
        print(f'Среднее число {b}')
    elif b < a < c or c < a < b:
        print(f'Среднее число {a}')
    else:
        print(f'Среднее число {c}')
except:
    print("Нужно было вводить три числа через пробел")