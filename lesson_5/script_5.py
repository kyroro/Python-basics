# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('script_5.txt', 'w') as f:
    f.write('1 2 3 4 5')

with open('script_5.txt') as f:
    num = f.read().split()
    sum = 0
    for i in num:
        sum += int(i)

print(sum)


