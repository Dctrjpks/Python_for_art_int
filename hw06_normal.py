# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random
class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor
    def _loss(self, person, strike, armor):
        person.health -= strike / armor
    def strike(self, damage):
        strike = damage
        return strike

class Player(Person):
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

class Enemy(Person):
    def _():
        return _()

gamer = Player('-', 1000, 100, 1.2)
vrag = Enemy(990,101,1.1)
gamer.name = input("Input gamer's name: ")

print(gamer.name, gamer.health, gamer.damage, gamer.armor)
print(vrag.health, vrag.damage, vrag.armor)

q = input('Wanna fight? (y/n): ')
while q == 'y':
    str = (0.8+0.2*random.random()) * gamer.strike(gamer.damage)
    vrag._loss(vrag, str, (0.8+0.3*random.random()) * vrag.armor)
    print('strike = ', round(r,2)
    # print('loss = ', s)
    print(gamer.name, round(gamer.health,2), gamer.damage, gamer.armor)
    print('vrag', round(vrag.health,2), vrag.damage, vrag.armor)
    print('Nice try! Enemy fights back!')
    strr = (0.8+0.2*random.random()) * vrag.strike(gamer.damage)
    gamer._loss(gamer, rr, (0.8+0.2*random.random()) * gamer.armor)
    print(40*"-")
    print(gamer.name, round(gamer.health, 2), gamer.damage, gamer.armor)
    print('vrag', round(vrag.health, 2), vrag.damage, vrag.armor)
    q = input('Shall we go on? (y/n): ')
