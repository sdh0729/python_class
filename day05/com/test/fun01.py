#인수, 매개인자 사용법

def my_fun(a,b,c):
    print(f'a={a} b={b} c={c}')

def my_fun01(a,b,/,c):
    print(f'a={a} b={b} c={c}') #/가 선언되면 /뒤에 나오는 변수는 키워드로 사용하겠다

if __name__ == '__main__':
    my_fun(10,20,30) # 순서대로 대입, 개수 맞아야함
    my_fun(a=1, b=2, c=3)
    my_fun01(1, 2, c=3) #my_fun(a=1, b=2, c=3) 에러