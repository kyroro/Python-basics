# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


list_1 = []
user_num = int(input('Введи кол-во цифр'))
current = 0

while user_num > current:
    num = int(input('Введите число'))
    list_1.append(num)
    current += 1
current_1 = 0
if len(list_1) > 1:
    while current_1 < len(list_1) - 1:
        list_1[current_1], list_1[current_1 + 1] = list_1[current_1 + 1], list_1[current_1]
        current_1 += 2

print(list_1)
