# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите строку')
counter = 0
for i in user_str.split():
    counter += 1
    print(f'{counter}.{i[:10]}')