# 7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

kilometer = int(input('Введите сколько километров пробегает спортсмен в первый день'))
purpose = int(input('Введите сколько нужно пробежать спортсмену'))
daus = 1

while kilometer < purpose:
    kilometer *= 1.1
    daus += 1
print(f'За {daus} дней')
