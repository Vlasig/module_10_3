import threading
from time import sleep
from random import randint
from threading import Lock


class Bank:
    def __init__(self):
        super().__init__()
        self.lock = Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            replenishment = randint(50, 500)
            self.balance += replenishment
            print(f"Пополнение: {replenishment}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdraw = randint(50, 500)
            print(f"Запрос на {withdraw}")
            if self.balance >= withdraw:
                self.balance -= withdraw
                print(f"Снятие: {withdraw}. Баланс: {self.balance}")
            else:
                self.lock.acquire()
                print("Запрос отклонён, недостаточно средств")
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
