'''
Exam02)
4. 제공된 데이터를 이용하여 웹서버의 특정 사용자에게 서비스한 데이터의 용량을 계산하는 코드를 작성하시오.
-> 0번째, 9번째 인덱스
'''
ip = input("Enter IP : ")
ip_cnt = 0
filename = '/Users/dhshin/PycharmProjects/python_class/Day10/access_log'
with open(filename) as f :
    lines = f.readlines()
    for i in range(len(lines)) :
        info = lines[i].split(' ')
        if ip == info[0] :
            dtsize = info[9][:-1]
            if '0' <= dtsize <= '99432' :
                ip_cnt += int(dtsize)

print(f"A amount of total serviced data to {ip} : {ip_cnt}")