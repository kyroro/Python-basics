# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыри'
}

with open('script_4.txt') as f, open('translator_script_4.txt', 'w') as fail:
    content = f.readlines()
    for i in content:
        delimiter = i.split()
        translator_number = num.get(delimiter[0])
        fail.writelines(f'{i.replace(delimiter[0], translator_number)}')
