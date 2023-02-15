import matplotlib.pyplot as plt
#<리스트 객체의 인덱스값 리턴 / ord(), chr() 시각화>
print('1. 일반 for 문을 이용해서 값을 출력 해보자')
my_list=['멍멍이', '야옹이', '꽥꽥이']
for w in my_list:
    print(w, len(w))
print(my_list[0][0])
print(my_list[1])
print(my_list[2])

'''
print('2. 일반 문자열 for 문을 이용해서 값을 출력 해보자')
my_list='일반 문자열 for 문을 이용해서 값을 출력 해보자'
for w in my_list: #문자열도 인덱스로
    print(w,len(w))
'''
print('3. for 문을 이용해서 값을 출력해보자 영문자 출력의 연습')
print('\n 영문자로 이루어진 글자중에서 각 문자의 빈도를 알고싶다')

word = 'abcezzzzzz'*2
h_res=[0]*26
print(h_res, end='\n')
print()
for c in word:
    h_res[ord(c)- ord('a')] +=1
print(h_res)

#plt.plot(h_res) # 그래프 Line 2D 그래프
#plt.show() #그래프 표시
print('4. for 문을 이용해서 값과 객체를 출력할 수 있는 구문을 시각화 해보자')
print('\n 영소문자로 이루어진 글자중에서 각 문자의 빈도를 알고 싶다')

left = list(range(26)) # 0~25
labels = [chr(i + ord('a')) for i in range(26)]
plt.bar(left, h_res, tick_label = labels)
plt.show()