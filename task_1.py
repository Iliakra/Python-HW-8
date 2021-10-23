""" Красильников Илья
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
 год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_to_num(cls, date_str):
        date_list = date_str.split('-')
        for el in date_list:
            print(int(el))

    @staticmethod
    def date_validate(date_str):
        date_list = date_str.split('-')
        if 0 < int((date_list[1])) < 12:
            print("Дата корректна")
        else:
            print("Неверно введен номер месяца в дате")


Data.date_to_num("12-03-2020")
mc = Data("12-03-2020")
mc.date_to_num("12-03-2020")
mc.date_validate("12-13-2020")



