'''
Exam02)
1. 제공된 데이터를 이용하여 웹서버 로그(본 페이지 수, 서비스를 요청한 페이지수)를 처리하는 코드를 작성하시오.
-> readLine()으로 읽어서 split() ==> 8번째 인덱스를 기준으로 상태값이 '200'
'''

cnt = 0
filename = '/Users/dhshin/PycharmProjects/python_class/Day10/access_log'
with open(filename) as f :
    lines = f.readlines()
    for i in range(len(lines)) :
        info = lines[i].split(' ')
        if info[8] == '200' :
            cnt += 1

print("Web server log: ", cnt)