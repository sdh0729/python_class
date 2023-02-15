print('1. 만약에 a=10 대입하고 a가 홀수 이면 홀수 짝수면 짝수라고 출력: 일반구문 ')
a=10
if a%2 !=0 :
    x = '홀수'
else :
    x = '짝수'
print(x.strip('수')) # jpg

print('2. 만약에 a=10 대입하고 a가 홀수 이면 홀수 짝수면 짝수라고 출력: 파이썬 구문 ')
a=10
x = {False : '짝수', True : '홀수'}[a%2].strip('수')
print(x)