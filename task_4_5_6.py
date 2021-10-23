""" Красильников Илья
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

Также задания 5,6
"""


class OnlyNumException(Exception):
    def __init__(self, text):
        self.text = text


class Storage:
    def __init__(self):
        self.storage_dict = {"printer": 0, "scanner":  0, "xerox":  0}
        self.items = []

    def add_to_storage(self, item):
        self.items.append({"name": item.tech_type, "title": item.name})
        self.storage_dict.update({item.tech_type: len(list(filter(lambda el: el["name"] == item.tech_type, self.items)))})

    def get_from_storage(self, item):
        for index, el in enumerate(self.items):
            if el["title"] == item.name:
                self.items.pop(index)
        self.storage_dict.update({item.tech_type: len(list(filter(lambda i: i["name"] == item.tech_type, self.items)))})


class OrgTechnics:
    def __init__(self, tech_type, manufacturer_name, year_of_produce):
        self.tech_type = tech_type
        self.name = manufacturer_name
        try:
            if not isinstance(year_of_produce, int):
                raise OnlyNumException("Год выпуска должен быть введен только числом!")
            # else:
            #     self.year = year_of_produce
        except OnlyNumException as err:
            print(err)

        else:
            self.year = year_of_produce


class Printer(OrgTechnics):
    def __init__(self, tech_type, manufacturer_name, year_of_produce, work_type, color):
        super().__init__(tech_type, manufacturer_name, year_of_produce)
        self.type = work_type
        self.color = color


class Scanner(OrgTechnics):
    def __init__(self, tech_type, manufacturer_name, year_of_produce, work_type, color, size):
        super().__init__(tech_type, manufacturer_name, year_of_produce)
        self.type = work_type
        self.color = color
        self.size = size


class Xerox(OrgTechnics):
    def __init__(self, tech_type, manufacturer_name, year_of_produce, work_type, color, size, speed):
        super().__init__(tech_type, manufacturer_name, year_of_produce)
        self.type = work_type
        self.color = color
        self.size = size
        self.speed = speed


my_storage = Storage()
print(my_storage.storage_dict)

my_printer_1 = Printer('printer', "HP", 2008, "laser", "multicolor")
my_printer_2 = Printer('printer', "Samsung", 2012, "struyny", "wb")
my_printer_3 = Printer('printer', "Deck", 2015, "struyny", "mu;ti")

my_scanner_1 = Scanner('scanner', "HP", 2015, "laser", "multicolor", "big")
my_scanner_2 = Scanner('scanner', "Pan", 2014, "laser", "wb", "small")

my_xerox_1 = Xerox('xerox', "Panasonic", 2020, "analog", "multicolor", "big", "fast")
my_xerox_2 = Xerox('xerox', "HP", 2005, "analog", "wb", "small", "slow")


my_storage.add_to_storage(my_printer_1)
my_storage.add_to_storage(my_printer_2)
my_storage.add_to_storage(my_printer_3)

my_storage.add_to_storage(my_scanner_1)
my_storage.add_to_storage(my_scanner_2)

my_storage.add_to_storage(my_xerox_1)
my_storage.add_to_storage(my_xerox_2)

print(my_storage.storage_dict)
print(my_storage.items)

my_storage.get_from_storage(my_printer_3)
my_storage.get_from_storage(my_xerox_1)

print(my_storage.storage_dict)
print(my_storage.items)

print(my_printer_1.year)
