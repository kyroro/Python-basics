# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число'))
max_number = 0
while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
    number //= 10

print(f'Самая большая цифра {max_number}')
