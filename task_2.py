""" Красильников Илья
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


my_input_1 = input("Введите делимое ")
my_input_2 = input("Введите делитель ")

try:
    num_1 = int(my_input_1)
    num_2 = int(my_input_2)
    if num_2 == 0:
        raise MyZeroDivError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не числа")
except MyZeroDivError as err:
    print(err)
else:
    print(int(num_1) / int(num_2))

