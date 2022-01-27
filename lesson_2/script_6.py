# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
#

products = []
counter = 1
command = ''
while command != 'stop':
    name = input('name')
    price = input('price')
    amount = input('amount')
    units = input('units')
    products.append(
        (counter, {'name': name, 'price': price, 'amount': amount, 'units': units})
    )
    counter += 1
    command = input('Write "stop" for stop inputting:')
print(products)

result_dict = {}

for numb, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_dict.get(key):
            result_dict[key] = [value]
        else:
            result_dict[key].append(value)

for key, value in result_dict.items():
    result_dict[key] = list(set(value))

print(result_dict)
