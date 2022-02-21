# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:

    @staticmethod
    def divide_by_null():
        try:
            divider = int(input('Введите делитель'))
            dividend = int(input('Введите диелимое'))
            return divider / dividend
        except ZeroDivisionError:
            return ("Делить на ноль нельзя")


div = DivisionByNull()
print(div.divide_by_null())
