# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

work_per_hour = int(argv[1])
rate_per_hour = int(argv[2])
premium = int(argv[3])


def result(work, rate, prem):
    return (work * rate) + prem


print(result(work_per_hour, rate_per_hour, premium))
