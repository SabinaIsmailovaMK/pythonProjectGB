#Задание 1
my_file = open('my_file.txt', 'w')
text = input('Введите текст \n')
while text:
    my_file.writelines(text)
    text = input('Введите текст \n')
    if not text:
        break

my_file.close()
my_file = open('my_file.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()

#Задание 2
my_file = open('my_file.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('my_file.txt', 'r')
content = my_file.readlines()
print(f'К-во строк в файле - {len(content)}')
my_file = open('my_file.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'К-во символов в строке № {i + 1} - {len(content[i])}')
my_file = open('my_file.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее к-во слов - {len(content)}')
my_file.close()
#Задание 3
with open('empl.txt', 'r') as my_file:
    zp = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        zp.append(i[1])
print(f'Вознаграждение меньше 20 000 у.е - {poor}')
print(f'Cредняя величина дохода сотрудников - {sum(map(float, zp)) / len(zp)} у.е')
#Задание 4
dict_rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_f = []
with open('count.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_f.append(dict_rus[i[0]] + '  ' + i[1])
    print(new_f)

with open('count_2.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_f)

#Задание 5
def func():

    with open('num.txt', 'w+') as file_obj:
        line = input('Введите цифры: ')
        file_obj.writelines(line)
        num = line.split()
        print(sum(map(float, num)))
func()

#Задание 6
subj = {}
with open('sabj.txt', 'r') as my_f:
    for line in my_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Название предмета и общее количество занятий по нему -  {subj}')

#Задание 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('info_company.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = float(earning) - float(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль составляет - {prof_aver:.2f}')
    else:
        print(f'Закрывайте лавочку!')
    profit.update(pr)
    print(f'Прибыль по отдельным компаниям - {profit}')

