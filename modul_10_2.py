from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            if enemies == 100:
                print(end="\n"f'{self.name}, на нас напали!')
            enemies -= self.power
            if enemies < 0: enemies = 0
            print(end="\n"f'{self.name} сражается {days} день(дня), осталось {enemies} воинов врага.')
        print(end="\n"f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(end="\n"'Все битвы закончились!')
