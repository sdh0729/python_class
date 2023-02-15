'''
Exam02)
2. 제공된 데이터를 이용하여 웹서버 방문자 수를 계산하는 코드를 작성하시오.
(동일한 IP를 갖는 클라이언트가 웹 사이트에 여러 번 접속하더라도 한 사람이 방문한 것으로 계산할 것.)
-> 0번째 인덱스 .. ip 개수를 세리면 됨/ 중복제거
'''

res = []
cnt = 0
filename = '/Users/dhshin/PycharmProjects/python_class/Day10/access_log'
with open(filename) as f :
    lines = f.readlines()
    for i in range(len(lines)) :
        info = lines[i].split(' ')
        res.append(info[0])

print("a number of visitors : ", len(list(set(res))))
