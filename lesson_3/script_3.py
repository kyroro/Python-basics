# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    number_max_1 = max(my_list)
    my_list.remove(number_max_1)
    number_max_2 = max(my_list)
    print(number_max_1 + number_max_2)


my_func(9, 6, 7)
