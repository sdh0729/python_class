#추상클래스와 다형성을 구현해보자
#추상클래스는 추상메소드를 선언해서 후손 클래스들이 강제로 재정의 할 수 있도록 한다
#1) 추상클래스는 객체생성이 불가능하다
#2) 추상클래스를 상속받는 후손 클래스는 선조의 추상메소드를 재정의 해야한다
#3) 추상클래스를 상속받는 후손 클래스는 선조의 추상메소드를 재정의 하지 않을 경우 후손클래스는 추상클래스가 된다

from abc import abstractmethod, ABCMeta

class Base(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        print("base start")
    @abstractmethod
    def Stop(self):
        print("base stop")

class Cat(Base):
    def start(self):
        print("cat start")
    def Stop(self):
        print("cat stop")

class Duck(Base):
    def start(self):
        print("duck start")
    def Stop(self):
        print("duck stop")

class puppy(Base):
# 선조의 추상메소드를 재정의 하지 않아서 추상클래스가 됬다. 추상메소드 = Stop()
# __abstractmethods__ = frozenset({'Stop'})
    def start(self):
        print("puppy start")
    def Stop(self):
        print("puppy stop")

class My(puppy):
    def Stop(self):
        print("My stop")
#동적 바인딩으로 구현할 수 있는 메소드

def my_call(m):
    m.start()
    m.Stop()

if __name__ == '__main__':
    my_call(My())
    my_call(Cat())
    my_call(Duck())
    #a1=Base()