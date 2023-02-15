'''
exam03) 애국가 1절에서 4절까지 myexam.txt로 저장된 것을 읽어서 다음과 같은 조건으로 구현한다.
        [조건1 ] 아래와 같이 파일에서 읽어온 문자열에서 단어를 찾아 카운트한다.(find함수 찾아서 한다)
        무궁화 : 000개
        대한사람 : 00개
        화려강산 : 00개
        백두산 : 00개
        [조건2 ] 위의 개수를 시각화 한다.

'''
import matplotlib.pyplot as plt
import re

file = open('myexam.txt','r',encoding='UTF-8')

text = file.read()

a = text.count('무궁화')
b = text.count('대한사람')
c = text.count('화려강산')
d = text.count('백두산')

e = [a,b,c,d]

f = re.findall('무궁화',text)
g = re.findall('대한사람',text)
h = re.findall('화려강산',text)
i = re.findall('백두산',text)

print(f)
print(g)
print(h)
print(i)

print(e)

print('무궁화 :', a, '개')
print('대한사람 :',b, '개')
print('화려강산',c, '개')
print('백두산',d, '개')

plt.plot(e)
plt.show()