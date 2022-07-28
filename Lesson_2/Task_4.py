"""Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
...Количество элементов (n) вводится с клавиатуры."""

def progresion_sum():
    n = input('Введите  число ')
    q = -0.5
    b_1 = 1
    if n.isdigit() == True:
        n = int(n)
        sum_n = (b_1 * ((q ** n) - 1))/(q - 1)
    else:
        print('В следующий раз введите число')
    print(f'Сумма n элементов  {sum_n}')

def main():
    progresion_sum()

if __name__ == '__main__':
    main()