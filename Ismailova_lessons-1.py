#Задание 1
a = 5
print(a)

name = (input('Введите Ваше прекрасное имя: '))
print(f'Добрейший вечерочек, {name}!')
age = (int(input('Сколько тебе лет, мой нежный(ая)? ')))
print(f'В возрасте {age} лет(года) тебе бы в баре сидеть, а не вот это вот все!')

#Задание 2
time = (int(input('Введите время в секундах: ')))
hour = (time//3600)
min = ((time-(hour*3600))//60)
sec = (time-(hour*3600+min*60))
print(f'Time- {hour}:{min}:{sec}')

#Задание 3
n = int(input('Введите число: '))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(f"После хитртоумных вычислений, Ваше число стало равно: {total}")

#Задание 4
a = abs(int(input('Введите целое положительное число: ')))
max = a % 10
while a >= 1:
    a = a//10
    if a % 10 > max:
        max = a % 10
    elif a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

#Задание 5-6

revenue = (float(input('Введите сумму выручки: ')))     # выручка
costs = (float(input('Введите сумму издержек: ')))      # издержки
if revenue > costs:
    print(f'У вас все хорошо! Размер прибыли составляет: {round((revenue-costs)/revenue*100,2)}%') # прибыль
    count_empl = abs(int(input('Введите количество сотрудников, чтобы оценить, как Вы хороши: ')))   # кол-во_сотрудников
    print(f'Только посмотри какой ты красавчик! Доход на одного сотрудника составляет {round((revenue-costs)/count_empl,2)}') #доход на 1 сотрудника
elif revenue == costs:
    print('Вы на грани!')
else:
    print('Запишитесь на кружок вязания!')

#Задание 7
a = (int(input('Введите первый рзультат: ')))                       # первый результат
b = (int(input('Введите результат, которого хотите достичь: ')))    # исомый результат
day = 1
result = a
while result < b:
    a = a + 0.1 * a     #10%
    day += 1            # day = day + 1
    result = result + a
print(f'Вы достигнете желаемого результата на {day} день')
