'''
Exam02)
3. 제공된 데이터를 이용하여 웹서버 총 서비스한 데이터의 용량을 계산하는 코드를 작성하시오.
(계산 단위는 KB로 함.)
-> 9번째 인덱스
'''
dtsizes = []
tot = 0
filename = '/Users/dhshin/PycharmProjects/python_class/Day10/access_log'
with open(filename) as f :
    lines = f.readlines()
    for i in range(len(lines)) :
        info = lines[i].split(' ')
        dtsizes.append(info[9][:-1])

        for j in range(len(dtsizes)) :
            if '0' <= dtsizes[j] <= '99432' :
                tot += int(dtsizes[j])

print("Total serviced data : ",tot)