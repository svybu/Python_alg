" Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."
number = input('Введите трехзначное число ')
sum = 0
result = 1
if len(number) == 3 and number.isdigit() == True:
    for i in number:
        sum = int(i) + sum
        result = int(i) * result
    print(sum, result)
else:
    print("нужно было ввести трехзначное число")
