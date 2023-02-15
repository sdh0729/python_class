class Operator:        

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

    def div(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

        return self.num1 / self.num2

    def mul(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

        return self.num1 * self.num2


op = Operator()

print('add:', op.add(20,10))
print('sub:', op.sub(20,10))
print('mul:', op.mul(20,10))
print('div:', op.div(20,10))
