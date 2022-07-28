"""Напишите программу, доказывающую или проверяющую, что для множества
 натуральных чисел  выполняется равенство: 1+2+...+n = n(n+1)/2, где
 n - любое натуральное число."""

def check():
    num = int(input('Введите целое число '))
    sum = 0
    sum_for_check = (num * (num + 1))/2
    for i in range(1, num+1):
        sum = sum + i

    if sum == sum_for_check:
        print(f'Все правильно {sum} = {sum_for_check}')
    else:
        print(f'не сошлось {sum} не равно {sum_for_check}')
    print()
def main():
    check()

if __name__ == '__main__':
    main()