try:
    a, b, c = map(float, input('ВВедите длину отрезков через пробел ').split())
    if a < (b + c) and b < (a + c) and c < (a + b):
        print('Такой треугольник может существовать ')
    else:
        print('Такой треугольник  не может существовать ')
except:
    print('Похоже, вы ввели неправильные данные( ')