"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""
result = {}

for i in range(2, 9):
    result[i] = []
    for j in range(2, 99):
        if j % i == 0:
            result[i].append(j)
    print(f' Для числа {i} есть {len(result[i])} кратных чисел. Это {result[i]}')
