#Задание 1
import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ''
        for i in range(len(self.matrix)):
            a = a + '\t'.join(map(str,self.matrix[i])) + '\n'
        return a

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)

l1 = [[1,2,4],[3,4,5],[5,6,6]]
l2 = [[11,21,41],[31,41,51],[51,61,61]]
b = Matrix(l1)
a = Matrix(l2)
print(b)
print(a)
m = b + a
print('Искомая матрица')
print(m)
print(type(m))

#Задание 2
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def consumption(self):
        return self.param * 2 + 0.3


a = Coat(52)
b = Suit(1.80)
print(a)
print(a.consumption)
print({b.consumption})


#Задание 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Cells {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity \
            if (self.quantity - other.quantity) > 0 \
            else print('Разность количества ячеек двух клеток меньше нуля')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(12)
cells2 = Cell(5)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells1.make_order(5))
print(cells2.make_order(12))
print(cells1 / cells2)