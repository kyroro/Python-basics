# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, date):
        Data.date = date

    @classmethod
    def int_num(cls, date):
        day = int(cls.date[:2])
        month = int(cls.date[3:5])
        age = int(cls.date[6:10])
        result = f'{day}.{month}.{age}'
        return result

    @staticmethod
    def date_validation(day, month, age):
        if day < 31 and day > 0:
            print('Валидация пройдена')
        if month < 13 and month > 0:
            print('Валидация пройдена')
        if age > 0:
            print('Валидация пройдена')
        else:
            print('Валидация не пройдена')


s = Data('11.09.2015')
s.int_num('11.09.2015')
s.date_validation(11, 12, 2001)
