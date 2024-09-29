from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name: str, power: int):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_ = 0
        enemy = 100
        while enemy > 0:
            enemy -= self.power
            count_ += 1
            time.sleep(1)
            print(f'{self.name} сражается {count_} день(дня)..., осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {count_} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
