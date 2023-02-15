'''
Exam01)

1. 제공된 데이터를 이용하여 이름, 성별, 출생아 수를 연도별로 계산하는 코드를 작성하시오
   결과를 birth.csv로 저장
for y range(1880,2016) :
    filename = '경로/yob{}.txt'.format(y)
'''
import csv

res = []
for i in range(1880, 2016) :
    filename = '/Users/dhshin/PycharmProjects/python_class/Day10/EXAM01_출생아데이터/yob{}.txt'.format(i)

    with open(filename) as f :
        lines = f.readlines()
        g_cnt = 0
        b_cnt = 0
        for j in range(len(lines)) :
            name, gender, cnt = lines[j].split(',')
            if gender == 'F' :
                g_cnt += int(cnt)
            elif gender == 'M' :
                b_cnt += int(cnt)
        res.append([i, g_cnt, b_cnt])
for i in range(len(res)) :
    print(f"{res[i][0]}year \ta number of baby girl borned  : {res[i][1]} \ta number of baby boy borned : {res[i][2]}")

with open('/Users/dhshin/PycharmProjects/python_class/Day10/EXAM01_출생아데이터/birthday.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(res)