# Задание 1

# class Date:
#     def __init__(self, dd_mm_yy):
#         self.dd_mm_yy = str(dd_mm_yy)
#
#     @classmethod
#     def extract(cls, dd_mm_yy):
#         my_date = []
#
#         for i in dd_mm_yy.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'Все введено верно'
#                 else:
#                     return f'Год введен некорректно'
#             else:
#                 return f'Месяц введен некорректно'
#         else:
#             return f'День введен некорректно'
#
#     def __str__(self):
#         return f'Текущая дата {Date.extract(self.dd_mm_yy)}'
#
#
# today = Date('14 - 2 - 2022')
# print(today)
# print(Date.valid(11, 11, 2055))
# print(today.valid(14, 15, 2022))
# print(Date.extract('14 - 2 - 2021'))
# print(today.extract('14 - 2 - 2022'))
# print(Date.valid(29, 1, 1994))

#Задание 2

# class Exeception_null:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return (divider / denominator)
#         except:
#             return (f"Внимание! Деление на ноль!")
#
#
# div = Exeception_null(5, 10)
# print(Exeception_null.divide_by_null(5, 0))
# print(Exeception_null.divide_by_null(10, 5))
# print(div.divide_by_null(10, 0))

#Задание 3

# class My_exception:
#     def __init__(self):
#         self.param = []
#     def my_input(self):
#         while True:
#             try:
#                 val = int(input('Ведите число: '))
#                 self.param.append(val)
#                 print(f'Текущий список - {self.param}')
#             except:
#                 print('Введено не число')
#
# try_except = My_exception()
# print(try_except.my_input())

# #Задание 4-6
#
# class Warehouse:
#
#     def __init__(self, brand, price, count, number_of_lists, *args):
#         self.brand = brand
#         self.price = price
#         self.count = count
#         self.numb = number_of_lists
#         self.my_warehouse_full = []
#         self.my_warehouse = []
#         self.my_unit = {'Бренд': self.brand, 'Цена': self.price, 'Количество': self.count}
#
#     def __str__(self):
#         return f'{self.brand} цена {self.price} количество {self.count}'
#
#     def reception(self):
#         # print(f'Для выхода - Q, продолжение - Enter')
#         try:
#             unit_b = input(f'Введите бренд ')
#             unit_p = int(input(f'Введите цену  '))
#             unit_c = int(input(f'Введите количество '))
#             unique = {'Бренд': unit_b, 'Цена за ед': unit_p, 'Количество': unit_c}
#             self.my_unit.update(unique)
#             self.my_warehouse.append(self.my_unit)
#             print(f'Текущий список -\n {self.my_warehouse}')
#         except:
#             return f'Ошибка ввода данных'
#
#         print(f'Для выхода - Q, продолжение - Enter')
#         q = input(f'---> ')
#         if q == 'Q' or q == 'q':
#             self.my_warehouse_full.append(self.my_warehouse)
#             print(f'Список техники на складе -\n {self.my_warehouse_full}')
#             return f'Выход'
#         else:
#             return Warehouse.reception(self)
#
#
# class Printer(Warehouse):
#     def to_print(self):
#         return self.numb
#
#
# class Scanner(Warehouse):
#     def to_scan(self):
#         return self.numb
#
#
# class Copier(Warehouse):
#     def to_copier(self):
#         return self.numb
#
#
# unit_1 = Printer('Xiaomi', 1400, 18, 1)
# unit_2 = Scanner('Canon', 2200, 23, 2)
# unit_3 = Copier('Xerox', 1500, 31, 3)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
# print(unit_1.to_print())
# print(unit_3.to_copier())

#Задание 7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.с = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма:')
        return f'с = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение:')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(-3, 6)
c_2 = ComplexNumber(2, 8)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
