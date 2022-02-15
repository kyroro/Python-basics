# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.


my_list = []
command = ' '
while command != '':
    command = input('Введите данные')
    my_list.append(f'{command}\n')

with open('script_1.txt', 'w', encoding='utf-8') as f:
    f.writelines(my_list)
