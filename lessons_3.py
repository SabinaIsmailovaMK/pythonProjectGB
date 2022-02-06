# #Задание 1
# arg_1 = int(input('Введите первый аргумент - '))
# arg_2 = int(input('Введите второй аргумент - '))
#
# def my_sum(arg_1, arg_2):
#     return arg_1 + arg_2
#
# print(my_sum(arg_1, arg_2))
#
# def my_div(arg_1, arg_2):
#     return arg_1 / arg_2
#
# if arg_2 == 0:
#     print ('Error')
# else:
#     print (my_div(arg_1, arg_2))
#
# #Задание 2
# arg_1 = input('First name - ')
# arg_2 = input('Last name - ')
# arg_3 = input('Email- ')
# arg_4 = input('City - ')
# arg_5 = int(input('tel - '))
#
# def my_inf(**kwargs):
#     return kwargs
# print (my_inf(F_name=arg_1, L_name=arg_2, Email=arg_3, City=arg_4, tel=arg_5))
#
# #Задание 3
# def my_func(*args):
#     args_1 = int(input("first args: "))
#     args_2 = int(input("second args: "))
#     args_3 = int(input("third args: "))
#
#     if args_1 >= args_2 > args_3:
#         return args_1 + args_2
#     elif args_3 >= args_2 > args_1:
#         return args_3 + args_2
#     elif args1 >= args_3 > args_1:
#         return args_1 + args_3
#     else:
#         exit(-1)
#
# print(my_func())

#Задание 4
def my_func(a,b):
    x1 = a ** b
    x2 = 1
    i = 1
    while i <= abs(b):
        x2 *= a
        i += 1

    return x1, 1 / x2

print(my_func(
        int(input("x1: ")),
        int(input("x2: "))))

#Задание 5
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 's' or number[el] == 'S':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Ваша итоговая сумма -  {sum_res}')
    print(f'Ваша итоговая сумма - {sum_res}')


my_sum()

#Задание 6

def func(a):
    return a.title()
print(func("sabina ismailova"))

def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()


