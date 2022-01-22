# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчёте на одного сотрудника.

profit = int(input('Введите выручку'))
costs = int(input('Введите издержки'))

if profit > costs:
    print('Прибыль')
    result_rent = (profit - costs) * profit
    print(f'Рентабельность {result_rent}')
    Employees = int(input('Введите кол-во сотрудников'))
    result_Employees = (profit - costs) / Employees
    print(f'Прибыль в рассчете на одного сотрудника состовляет {result_Employees}')
if profit < costs:
    print('Убытки')
