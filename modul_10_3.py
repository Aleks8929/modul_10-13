from random import randint
from time import sleep
from threading import Thread, Lock


class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = randint(50, 500)
            self.balance += x
            print(end="\n"f'Пополнение: {x}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            y = randint(50, 500)
            print(end="\n"f'Запрос на {y}')
            if self.balance >= y:
                self.balance -= y
                print(end="\n"f'Снятие: {y}. Баланс: {self.balance}')
            elif self.lock.locked():
                print(end="\n"f'Запрос отклонён, недостаточно средств')
            else:
                print(end="\n"f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(end="\n"f'Итоговый баланс: {bk.balance}')
