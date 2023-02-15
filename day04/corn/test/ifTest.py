print('1. 만약에 a가 5 보다 크면 *2를 하고 그렇지 않으면 /2로 나누자')
a=10
if a>5 :
    x = a * 2
else :
    x = a / 2
print(x)

print('2. 만약에 a가 5 보다 크면 *2를 하고 그렇지 않으면 /2로 나누자 : 파이썬 구문 ')
a =10
x= a*2 if a > 5  else a/2
print(x)

print('3. 만약에 a가 5 보다 크면 *2를 하고 그렇지 않으면 /2로 나누자 : 파이썬 구문 인덱스 형식 ')
a=10
res = (a/2, a*2)
x = res[a>5] # True: 1, False : 0
print(x)

print('4. 만약에 a가 5 보다 크면 *2를 하고 그렇지 않으면 /2로 나누자 : 3을 간단하게')
a=10
x = (a/2, a*2)[a>5] # True: 1, False : 0
print(x)