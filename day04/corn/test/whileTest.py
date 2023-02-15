#while 문은 while 조건식이 False 가 될 때까지 반복적으로 수행한다.
'''
while 조건식:
   명령;
while 조건식:
   명령;
else:
   False 명령
'''
a=1
while a>=5:
    print(a)
else:
    print('~~False~~')

x=1
sum=0
while x<=10 :
    sum += x
    x += 1
print(x,sum)

tot=0
for x in range(11):
    tot+=x
print(x, tot)

###########
i=1
j=0
while True:
    if i > 10:
        break
    else:
        print(i, '번째 반복입니다')
        print('합산한 값은 ', j, '입니다.\n')
        i=i+1  # i+=1
        j=j+1  # j+=1