# 메소드를 변수로 호출할 수 있도록 지칭 데코레이션 @property

class My:
    def __init__(self):
        self.x = 0

    @property #myFun.getter
    def myFun(self): #멤버 변수 x를 리턴하는 용도의 메소드 getter
        return self.x

    @myFun.setter
    def myFun(self,x): #멤버 변수 x에 값을 전달 및 변경 하는 용도의 메소드 setter
        self.x = x

if __name__ == '__main__':
    a = My()
    a.myFun = 100 #myFun.setter
    print(a.myFun) # @property  #myFun.getter




