#연산자 overoading
#클래스를 선언하게 되면 오브젝트 클래스의 멤버를 상속받아 사용하게 되는데 그중 연산자에 관련된 메소드를 재정의해서 사용하는 것

class MyClass:
    def __init__(self,su):
        self.su = su

    def __eq__(self, other): #self -> a, other -> b
        return self.su == other.su

    def __lt__(self, other): #self -> a, other -> b
        return self.su < other.su

    def __gt__(self, other): #self -> a, other -> b
        return self.su > other.su

if __name__ == '__main__':

    a = MyClass(100)
    b = MyClass(200)
    #생성자로 받은 값을 객체 비교로 연산 하고 싶다.
    print(a > b)  # 100 > 200
    print(a < b)  # 100 < 200
    print(a == b) # 100 == 200