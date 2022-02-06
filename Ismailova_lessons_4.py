# Задание 1
def zp():
    time = float(input('Количество отработанных часоов : '))
    stavka = int(input('Введите ставку/час : '))
    bonus = int(input('Премия - '))
    return (time * stavka) + bonus
print(f'Размер заработной платы составил: {zp()}')

# Задание 2
spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [Q for q, Q in zip(spisok, spisok[1:]) if Q > q]
print(f"Мой список: {spisok}")
print(f"Новый список: {new_list}")

# Задание 3
print(f'Числа от 20 до 240 кратные 20 или 21 - {[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]}')

# Задание 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list if my_list.count(i) < 2]
print(new_list)

# Задание 5
from functools import reduce

def func(i, el):
    return i * el

print(f'Четные значения - {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов - {reduce(func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Задание 6(1)
from itertools import cycle, count

start = int(input('Start num: '))
stop = start * 2 + 10 + 1

for i in count(start):
    if i < stop:
        print(i)
    else:
        break
del i

# Задание 6(2)

my_list = [i for i in range(stop)]
count = 0
for b in cycle(my_list):
    if count < stop + 10:
        print(b)
        count += 1
    else:
        break
