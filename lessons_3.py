#Задание 1
arg_1 = int(input('Введите первый аргумент - '))
arg_2 = int(input('Введите второй аргумент - '))

def my_sum(arg_1, arg_2):
    return arg_1 + arg_2

print(my_sum(arg_1, arg_2))

def my_div(arg_1, arg_2):
    return arg_1 / arg_2

if arg_2 == 0:
    print ('Ошибка')
else:
    print (my_div(arg_1, arg_2))

#Задание 2
arg_1 = input('First name - ')
arg_2 = input('Last name - ')
arg_3 = input('Email- ')
arg_4 = input('City - ')
arg_5 = int(input('tel - '))

def my_inf(**kwargs):
    return kwargs
print (my_inf(F_name=arg_1, L_name=arg_2, Email=arg_3, City=arg_4, tel=arg_5))

#Задание 3
def my_func(*args):
    arg_1 = int(input("first arg: "))
    arg_2 = int(input("second arg: "))
    arg_3 = int(input("third arg: "))

    if arg_1 >= arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_3 >= arg_2 > arg_1:
        return arg_3 + arg_2
    elif arg_1 >= arg_3 > arg_1:
        return arg_1 + arg_3
    else:
        exit(-1)

print(my_func())

#Задание 4
def my_func(x, y):
    a = x ** y
    b = 1
    i = 1
    while i <= abs(x):
        b *= a
        i += 1

    return a, 1 / b

print(my_func(
        int(input("x = ")),
        int(input("y = "))))

#Задание 5
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел- ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 's' or number[el] == 'S':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Ваша итоговая сумма -  {sum_res}')
my_sum()

#Задание 6
def func(a):
    return a.title()
print(func("sabina ismailova"))

def int_func (*args):
    word = input("Введите слова -  ")
    print(word.title())
    return
int_func()


