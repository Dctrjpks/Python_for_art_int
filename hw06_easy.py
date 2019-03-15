# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
    def go(self):
        print('Going...')
    def stop(self):
        print('Stopped !')
    def turn(self, direction):
        if direction == 'right':
            print('Turning right ->')
        if direction == 'left':
            print('Turning left <-')
        if direction == 'back':
            print('Turning back U')
class TownCar(Car):
    def __init__(self):
        self.speed = 100
        self.is_police = False
class SportCar(Car):
    def __init__(self):
        self.speed = 250
        self.is_police = False
class WorkCar(Car):
    def __init__(self):
        self.speed = 60
        self.is_police = False
class Police(Car):
    def __init__(self):
        self.is_police = True


