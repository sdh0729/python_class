import matplotlib.pyplot as plt
print("1. for 중첩을 연습해 보자")

my_list = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
    ['j','k','l']
] # 4*3 행렬 // 행 outer for // 열 inner for

for i in range(4): # 0~3
    for j in range(3): # 0~2
        print('my_list', i+1, '번째 행의 ',j+1,'번째 목록= ',my_list[i][j])

print('2. for 중첩을 가지고 시각화를 활용해 보자')
res = [[1]]

for i in range(100):
    res.append([1]+[0] * i +[1])
    for j in range(i):
        res[i+1][j+1] = res[i][j] + res[i][j+1]
print(res[:10])
plt.plot(res[100])
plt.show()
'''
for x in 목록:
   요소 x에 대한 처리 ---> 계산량 : 알고리즘을 기초로 한 프로그램의 실행 시간 견적하는 지표
-> 요소에 대한 처리가 요소수만큼 실행된다.
-> 처리시간이 일정하다면 요소 수 n, 전체 처리에 n은 비례하는 시간이 걸린. O(n) 라고 for를 표현한다

2*3 = 2행의 3열 = 3열을 2번 실행하겠다
for i in 목록:
   for j in 목록:
      ~(i,j)----->n**2
'''
