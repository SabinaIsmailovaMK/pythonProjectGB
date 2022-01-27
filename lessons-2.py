#Задание 1
int_a = 123
float_b = 1.5
str_c = 'Hello python'
typle_d = ('1', 'a', '4.5')
list_g = ['1', '4.6', 'b', '7']
dict_f = {'Джош Рэднор': 'Тед Мосби', 'Нил Харрис': 'Барни Стинсон'}

combo = [int_a, float_b, str_c, typle_d, list_g,dict_f]
for i in combo:
    print(f'{i} - {type(i)}')

#Задание 2
el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)


#Задание 3
num = int(input('Введите месяц от 1 до 12: '))
if num <= 12 and num >= 1:
    dict_month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    list_month = list(dict_month.values())
for i, el in enumerate(list_month):
    if num-1 == i:
        print(f'Ваш месяц - это {list_month[i]}')
        break

#Задание 4
my_str = input("Введите строку: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i} - {el}")

#Задание 5
spisok = [7, 5, 3, 3, 2]
print(spisok)
num = int(input('Введите число от 0 до 10: '))
while num <= 10 and num >= 0:
    for i in range(len(spisok)):
        if spisok[i] == num:
            spisok.insert(i+1, num)
            break
        elif spisok[0] < num:
            spisok.insert(0, num)
        elif spisok[-1] > num:
            spisok.append(num)
        elif spisok[i] > num and spisok[i + 1] < num:
            spisok.insert(i + 1, num)
    print(f"New список {spisok}")
    num = int(input("Введите число от 0 до 10: "))