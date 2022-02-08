# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

company = {}
profit_company = 0
general_sum = 0
with open('script_7.txt') as f:
    file = f.readlines()

for i in file:
    delimiter = i.split()
    profit = int(delimiter[2]) - int(delimiter[3])
    company.update({delimiter[0]: profit})
    if profit > 0:
        profit_company += 1
        general_sum += profit

mean_value = general_sum / profit_company
result = [company, {mean_value: 'mean_value'}]

with open('script_7.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
