import locale
locale.setlocale(locale.LC_ALL, '')

class Operator():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, balance):
        self.__balance += balance

    def withdraw(self, balance):
        self.__balance -= balance


class Account(Operator):
    def __init__(self, balance, num):
        self.__balance = balance
        self.num = num

    def numFormat(self, num):
        return locale.format_string('%d', num, 1)

    def getBalance(self):
        return self.numFormat(self.__balance)

    def deposit(self, balance):
        self.__balance += balance

    def withdraw(self, balance):
        self.__balance -= balance
