cnt = 0
with open('2.2kw_L-DEF-01_normal.csv', 'r', encoding = 'utf-8') as f:
    while True:
        data = f.readline()
        if not data:
            break
        cnt += 1
        
print(cnt)

