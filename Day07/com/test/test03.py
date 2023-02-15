# 다중상속
class Dog:
    def sound(self):
        print('bark')
    def Dog_prn(self):
        print('Dog_prn')
class Cat:
    def sound(self):
        print('meow')
    def Cat_prn(self):
        print('Cat_prn')

class Chimera(Dog, Cat):
    def sound(self):
        Dog.sound(self)
        Cat.sound(self)
        super().sound()
        super().Dog_prn()
        super().Cat_prn()
        print('chimera')

if __name__ == '__main__':
    Chimera().sound()