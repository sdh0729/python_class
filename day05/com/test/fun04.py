def my_fun(a,b,c):
    print(f'a={a} b={b} c={c}')
def my_fun1(a,b,c):
    pass # 제어문, 함수, 메소드, 예외처리구문, 클래스에 선언만 해놓을 경우 사용

if __name__ == '__main__':
    my_fun(10,20,30)
    my_list = [11,22,33]
    my_fun(*my_list) # 튜플이나 리스트 객채에 *를 붙이면 위치 매개인자로 간주한다
    my_dict = {'a':100, 'b':200, 'c':300}
    my_fun(**my_dict)