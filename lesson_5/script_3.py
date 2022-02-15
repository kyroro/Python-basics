# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('script_3.txt') as f:
    content = f.readlines()

workers = {}
sum = 0
for i in content:
    delimiter = i.split()
    workers = {delimiter[0]: int(delimiter[1])}
    sum += int(delimiter[1])
    if int(delimiter[1]) < 20000:
        print(f'{delimiter[0]} {delimiter[1]}')
average_value_income = sum / len(workers)
print(f'{average_value_income} - средняя величина дохода')
