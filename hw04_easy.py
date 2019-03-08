# Все задачи текущего блока решите с помощью генераторов списков!
#
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
n = 10
m = 9
list_integer = [random.randint(0,m) for i in range(n)]
print (list_integer)
list_square = [list_integer[i]**2 for i in range(n)]
print(list_square)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
#
fruit_1 = []
fruit_2 = []
fruit_all = ['Apple','Apricot','Avocado','Banana','Bilberry','Blackberry','Blackcurrant','Blueberry','Currant','Cherry','Cloudberry','Coconut','Cranberry','Elderberry','Feijoa','Fig','Gooseberry','Grape','Grapefruit','Guava','Huckleberry','Jackfruit','Kiwifruit','Kumquat','Lemon','Lime','Lychee','Mango','Mangosteen','Marionberry','Mulberry','Nectarine','Olive','Orange','Mandarine','Tangerine','Papaya','Passionfruit','Peach','Pear','Persimmon','Plum','Pineapple','Pomegranate','Pomelo','Raspberry','Redcurrant','Strawberry','Ugli fruit']
fruit_1 = [fruit_all[random.randint(0,len(fruit_all)-1)]for j in range(n) if fruit_all[j] not in fruit_1]
fruit_2 = [fruit_all[random.randint(0,len(fruit_all)-1)]for k in range(n) if fruit_all[k] not in fruit_2]
fruit_both = []
fruit_both = [fruit_2[l] for l in range(len(fruit_2)) if fruit_2[l] in fruit_1]
print (fruit_1)
print (fruit_2)
print (fruit_both)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_any_num = []
list_final = []
o = 50
p = 20
list_any_num = [random.randint(-o,o) for i in range(p)]
list_final = [list_any_num[ii] for ii in range(p) if list_any_num[ii]%3==0 and  list_any_num[ii] >=0 and list_any_num[ii] %4 != 0]


print(list_any_num)
print(list_final)
