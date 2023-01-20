# 1. Реализовать класс «Дата», функция-конструктор которого должна 
# принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. Первый, 
# с декоратором @classmethod. Он должен извлекать число, месяц, 
# год и преобразовывать их тип к типу «Число». Второй, 
# с декоратором @staticmethod, должен проводить валидацию числа, 
# месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.

from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('.')

    @classmethod
    def extract(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('.')]
            print(day, type(day),'\n',
                  month, type(month),'\n', 
                  year, type(year))
        except ValueError:
            print('Указана неправильная дата')

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('.')
            date(int(year), int(month), int(day))
            print('Указана правильная дата')
        except ValueError:
            print('Указана неправильная дата')


Data.valid('19.01.2023')
Data.extract('19.01.2023')