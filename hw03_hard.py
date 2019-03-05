# import this
# print(this)

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# def attack(person1, person2): # 1 - ATTACK 2 - DEFEND
#     person2['health'] -= person1['damage']
#     return person2
#
#
# player_name = input('Введите имя игрока: ')
# enemy_name = input('Введите имя противника: ')
#
# player = {'name': player_name, 'health':100, 'damage': 50}
# enemy = {'name': enemy_name, 'health':100, 'damage': 50}
#
# player = attack(enemy, player) # противник атакует игрока
#
# print(player)



# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def strike(person1, person2):
    strike = person1['damage'] / person2['armour']
    return strike
def attack(person1, person2): # 1 - ATTACK 2 - DEFEND
    person2['health'] -= strike(person1, person2)
    return person2
def write_file(dictionary): # записываем данные сущности в файл
    # a = dictionary['name']
    player_data = open((dictionary['name']+'.txt'), 'w', encoding='utf-8')
    player_data.write('{},{},{},{}'.format(dictionary['name'], dictionary['health'], dictionary['damage'], dictionary['armour']))
    player_data.close()
def read_file(file_name):# извлекаем данные сущности из файла в  словарь
    dictionary = {}
    file = open(file_name+'.txt', 'r', encoding='utf-8')
    file.close()
    return dictionary


player_name = input('Введите имя игрока: ')
enemy_name = input('Введите имя противника: ')

player = {'name': player_name, 'health':100, 'damage': 50, 'armour': 1.2}
enemy = {'name': enemy_name, 'health':100, 'damage': 50, 'armour': 1.2}
write_file(player)
write_file(enemy)
player = attack(enemy, player) # противник атакует игрока
write_file(player)

print(player['name'])
print(player)