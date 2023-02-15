'''
[형식]
def username():
   명령
   :return
'''

def My_fun(name):
    print(f'이름은 {name} 이다')
def U_fun():
    print(1,2,3,4,5)
def My_Sum(kor,eng,mat):
    tot = kor + eng + mat
    print(f'tot={tot}' )

if __name__ == '__main__':
    My_fun('홍길동') # 홍길동을 주면서 함수를 부르면 이름이 홍길동이다 라고 출력하는 함수
    U_fun()
    My_Sum(90,100,85)