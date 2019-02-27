# # Задача-1:
# # Дан список, заполненный произвольными целыми числами, получите новый список,
# # элементами которого будут квадратные корни элементов исходного списка,
# # но только если результаты извлечения корня не имеют десятичной части и
# # если такой корень вообще можно извлечь
# # Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print('')
print('Задача-1')
print('')
spisok = [2, -5, 8, 9, -25, 25, 4]
result = []
for _ in range(len(spisok)):
    if spisok[_] >= 0:
        a = spisok[_]**0.5
        if (a%1) == 0:
            result.append(int(a))
print (spisok)
print (result)




# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


print("")
print('Задача-2')
print('Если правильно ввести -  работает. Учёт ошибок не доделал')
print("")
#date = '18.12.2001'
range_one = ["никакое", "первое", "второе", "третье", "четвёртое", "пятое", "шестое", "седьмое", "воосьмое", "девятое", "десятое"]
range_two = ["никак", "один", "две", "три", "четыр", "пят", "шест", "сем", "восем", "девят"]
range_mon = ["нихеря", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
day_num = 10000
month_num = 10000
year_num = 10000
while year_num > 9999:
    while month_num > 12:
        while day_num > 31:
            date = input('Введите дату dd.mm.yyyy: ')
            if len(date) < 10:
                print("Такой даты не существует")
                break
            day = date[0:2]
            day_num = int(day)
            month = date[3:5]
            month_num = int(month)
            year = date[6:10]
            year_num = int(year)

            if day_num > 31:
                print("Такой даты не существует")

        continue
        if month_num > 12:
            print("Такой даты не существует")

    continue
    if (month_num == 4
    or month_num == 6
    or month_num == 9
    or month_num == 11) and (day_num > 30):
        print("Такой даты не существует")

    if month_num == 2 and (day_num > 29):
        print("Такой даты не существует")

    if month_num == 2 and year_num % 4 !=0 and (day_num > 28):
        print("Такой даты не существует")

if day_num>=0 and day_num<11:
    day_word = range_one[day_num]
if day_num>=11 and day_num<=19:
    day_word = range_two[day_num-10] + 'надцатое'
if day_num>=21 and day_num<=29:
    day_word = 'двадцать ' + range_one[day_num-20]
if day_num>=31 and day_num<=39:
    day_word = 'тридцать ' + range_one[day_num-30]
if day_num == 20:
    day_word = 'двадцатое'
if day_num == 30:
    day_word = 'тридцатое'
month_word = range_mon[month_num]
date_word = day_word + ' ' + month_word + ' '+ str(year_num) + ' года'
print(date_word)
print (date)
# print(type(date))
# print (day)
# print (month)
# print (year)



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print("")
print('Задача-3')
print("")

import random
imp = input('Введите целое число: ')
n = int(imp)
list_100 = []
for i in range(n):
    list_100.append(random.randint(0,100))
print (list_100)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("")
print('Задача-4')
print("")

lst = [1, 2, 4, 5, 6, 2, 5, 2]
print('lst: ', lst)
lll = set(lst)
lst1 = list(lll)
lst2 = []
print('lst1:',lst1)


for i in range(len(lst1)):
    f = 0
    for j in range(len(lst)):
        if lst1[i] == lst[j]:
            f += 1
    if f == 1:
        lst2.append(lst1[i])

        continue
print ('lst2:', lst2)
