#Задание 1
from time import sleep

class TrafficLight:
    __color = ['red', 'yelloy', 'green']
    def turn_on(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}', 'Ожидание...')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.turn_on()

#Задание  2

class Road:
    __length = None
    __width = None
    mass_m2 = None
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def pokrytie(self):
        self.mass_m2 = 25
        self.thickness = 0.05
        pokrytie = (self.length * self.width * self.mass_m2 * self.thickness)//1000
        print(f'Необходимо {pokrytie} тонн для покрытия всей дороги')

road = Road(20, 5000)
road.pokrytie()

#Задание 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position (Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name +' '+ self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Sabina', 'Ismailova ','Data analyst', 35000, 7000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

#Задание 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        return f'{self.name} вперёд'

    def stop (self):
        return f'{self.name} стоп'

    def turn_left(self):
        return f'{self.name} <<< левый поворот'

    def turn_right(self):
        return f'{self.name} правый поворот >>>'

    def show_speed(self):
        return f'{self.name} мчит со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Допустимая скорость для {self.name} это {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} больше допусттимого'
        else:
            return f'Скорость {self.name} в рамках допустимой скорости'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Допустимая скорость для {self.name} это {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой'
        else:
            return f'скорость {self.name} в пределах нормы'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


BMW = SportCar(130, 'graphite', 'BMW', False)
sneakers = TownCar(40,'multicolor' ,'sneakers' , False)
telega = WorkCar(30,'brown' ,'telega' , False)
tayota = PoliceCar(60,'white' ,'tayota' , True)

print(f'Шёл как-то {sneakers.go()} мимо,')
print(f'И стал свитетелем того, как {telega.turn_left()} включила. {BMW.stop()} вынужден был совершить.')
print(f'И {telega.color} транспортное средство едет на {telega.show_speed()}.')
print(f'Навстречу {tayota.color} рука закона, так ведь?  {tayota.is_police}')
print(f'{tayota.name} уволокла {telega.name}(у) вскорости в закат.')


#Задание 5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} - запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} - запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} - запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

