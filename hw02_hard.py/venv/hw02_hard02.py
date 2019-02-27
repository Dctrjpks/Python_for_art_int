# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

# def end_of_work():
#     return input('Спасибо за работу!')
date = input('Введите дату dd.mm.yyyy: ')
day = date[0:2]
day_num = int(day)
month = date[3:5]
month_num = int(month)
year = date[6:10]
year_num = int(year)
if day_num > 31 or day_num < 1:
    print('Дата некорректная 31')
    # end_of_work()
elif month_num > 12 or month_num < 1:
    print('Дата некорректная 12')
    # end_of_work()
elif year_num > 9999:
    print('Дата некорректная 9999')
    # end_of_work()

elif (month_num == 4
or month_num == 6
or month_num == 9
or month_num == 11) and (day_num > 30):
    print('Дата некорректная 30')
    # end_of_work()
elif month_num == 2 and (day_num > 29):
    print('Дата некорректная фев')
    # end_of_work()
elif month_num == 2 and year_num % 4 !=0 and (day_num > 28):
    print('Дата некорректная вис 2')
    # end_of_work()

else: print('Дата корректная')
# print(day_num, month_num, year_num)
# print (day, month, year)
# end_of_work()

