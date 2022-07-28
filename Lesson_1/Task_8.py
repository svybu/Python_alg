try:
    year = int(input('Введите год '))
    if year % 4 != 0 or (year % 100 ==0 and year % 400 != 0):
        print('Это обычний год')
    else:
        print('Это високосный год')
except:
    print("Нужно было вводить числа")
