"""1. Пользователь вводит данные о количестве предприятий, их наименования
 и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
 Программа должна определить среднюю прибыль (за год для всех предприятий)
 и вывести наименования предприятий, чья прибыль выше среднего и отдельно
 вывести наименования предприятий, чья прибыль ниже среднего."""
import collections
while True:
    try:
        n = int(input('ВВедите количество компаний '))
    except ValueError:
        print(' Некорректное значение( ')
        continue
    break
#companies = collections.defaultdict
companies = {}
total_income = 0
year_income = 0
avg_income = 0
#good_comp = collections.deque
#bad_comp = collections.deque  # на это и defaultdict постонно вылезали ошибки от которых не смог избавиться. Поэтому сделал через обычные списки и словарь
good_comp = []
bad_comp = []
for i in range(n):
    m = 1
    name = input('Введите название компании ')
    companies[name] = []
    i += 1
    while m <= 4:
        quart_income = float(input(f'ВВедите прибыль за {m} квартал '))
        companies[name].append(quart_income)
        year_income += quart_income
        if m == 4:
            companies[name].append(year_income) #сделано чтобы и оставались исходные данные за квартал и отдельно годовой доход
        m += 1
for i, item in companies.items():
    total_income += item[-1]
avg_income = total_income/n
for i, item in companies.items():
    if item[-1] < avg_income:
        bad_comp.append(i)
    else:
        good_comp.append(i)
print(f' В этих прибыль выше среднего {good_comp}'
      f' а в этих прибыль ниже  среднего {bad_comp}')
