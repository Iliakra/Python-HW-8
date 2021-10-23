""" Красильников Илья
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните
"""


class ComplexNum:
    def __init__(self, complex_num_str):
        self.complex_num = complex_num_str.split('i')[0]

    @property
    def num_generate(self):
        res_str = []
        num = ''
        for index, el in enumerate(self.complex_num):
            if not el.isnumeric() and index > 0:
                res_str.append(int(num))
                num = ''
                num += el
            elif index == len(self.complex_num)-1:
                num += el
                res_str.append(int(num))
                num = ''
            else:
                num += el
        return res_str

    def __add__(self, other):
        a = str(self.num_generate[0] + other.num_generate[0])
        b = str(self.num_generate[1] + other.num_generate[1]) + 'i'
        if b[0].isnumeric():
            b = "+" + b
        return a+b

    def __mul__(self, other):
        a = str(self.num_generate[0] * other.num_generate[0] - self.num_generate[1] * other.num_generate[1])
        b = str(self.num_generate[1] * other.num_generate[0] + self.num_generate[0] * other.num_generate[1]) + 'i'
        if b[0].isnumeric():
            b = "+" + b
        return a + b


c = ComplexNum("1+1i")
d = ComplexNum("1+4i")
print(c+d)
print(c*d)




