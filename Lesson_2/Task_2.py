"""Посчитать четные и нечетные цифры введенного натурального числа. Например,
 если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""
def count():
    num = input('Введите натуральное число ')
    count1 = 0
    count2 = 0
    if num.isdigit() == True:
        for i in num:
            i = int(i)
            if i % 2 == 0:
                count2 = count2 +1
            else:
                count1 = count1 +1
    else:
        print('В следующий раз введите число')
    print(f'В данном числе {count2} четных цыфры и {count1} нечетных')

def main():
    count()

if __name__ == '__main__':
    main()