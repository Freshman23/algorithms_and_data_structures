"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import defaultdict


enterprises_dict = defaultdict(list)
amount = int(input('Enter an amount of enterprises: '))
average_profit = 0
print('Enter information(name, quarter profits) about every enterprise,\n'
      'separated by a space like that(without quotes): "Insay 1000 1500 2000 1700".')

for i in range(amount):
    enterprise = input(f'Enterprise #{i + 1}: ').split(' ')
    profits = list(map(int, enterprise[1:]))
    enterprises_dict[enterprise[0]] = profits + [sum(profits)]
    average_profit += sum(profits)
average_profit /= amount

print(enterprises_dict)
print('Average profit:', average_profit)

ge_average = []
lt_average = []
for name, profits in enterprises_dict.items():
    if profits[4] >= average_profit:
        ge_average.append(name)
    else:
        lt_average.append(name)

print(f'Enterprises that have greater than or equal average profit: {ge_average}\n'
      f'Enterprises that have less than average profit: {lt_average}')
