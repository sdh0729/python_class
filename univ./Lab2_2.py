class Operator:
    
     def __init__(self, money = 0):
        self.money = money
    
     def add(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

        return self.num1 + self.num2

     def sub(self, num1, num2):
 
        self.num1 = num1
        self.num2 = num2

        if self.num1 >= self.num2:
            return self.num1 - self.num2

        else :
            return self.num2 - self.num1

     def setBalance(self):
         balance = self.money
         return balance

class Account(Operator):
    
    def __init__(self, money = 0):
        self.money = money

    def deposit(self, money):
        self.money = super().add(self.money, money)
        print('deposit', money)
        return self.money
    
    def withdraw(self, money):
        self.money = super().sub(self.money, money)
        print('withdraw', money)
        return self.money

    def getBalance(self):
        self.__balance = super().setBalance()
        return self.__balance

a=Account()
print('balance', a.getBalance())
a.deposit(30000)
print('balance', a.getBalance())
a.withdraw(20000)
print('balance', a.getBalance())
