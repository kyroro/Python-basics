# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

season = int(input('Введите месяц в виде числа'))

season_dict = {
    12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
    9: 'Осень', 10: 'Осень', 11: 'Осень'
}

print(season_dict[season])

season_list = ['Зима', 'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Лето', 'Лето', 'Лето']

print(season_list[int(season) - 1])