
class My:
    def __init__(self):
        print('My class 명시 생성자')
    '''
    def __del__(self):
        print('명시 소멸자')
    '''
class U:
    def __del__(self): # 객체를 소멸하는 메소드를 재정의하게 되면 명시된 소멸자가 호출되며 객체가 소멸된다
        print('u 명시 소멸자')
if __name__ == '__main__':
    print(dir(U))
    print(dir(My))

    m1=My()  #__init__ 명시 생성자로 호출
    u1=U()   #__init__ 기본 생성자 호츌

    del u1 # 전역으로 선언된 내장 명령으로 사용 되는 것, 생성된 객체 소멸
    print(dir())