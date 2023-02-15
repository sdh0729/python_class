'''
Exam01)
2. 1번에서 완성된 코드에 상위 5개 인기 이름을 출력하는 코드를 작성하시오
'''
f_res = []
m_res = []
filename = '/Users/dhshin/PycharmProjects/python_class/Day10/EXAM01_출생아데이터/yob2000.txt'

with open(filename) as f:
    lines = f.readlines()

    for j in range(len(lines)) :
        name, gender, cnt = lines[j].split(',')
        cnt = int(cnt)
        if gender == 'M' :
            m_res.append([name, cnt])
        else :
            f_res.append([name, cnt])

f_ans = sorted(f_res, key = lambda x : (x[1], x[0]), reverse=True)
m_ans = sorted(m_res, key = lambda x : (x[1], x[0]), reverse=True)

for i in range(5) :
    print(f"남자 {i+1}위 {m_ans[i][0]}가\t{m_ans[i][1]}명 \t여자{i+1}위 {f_ans[i][0]}가 \t{f_ans[i][1]}명")