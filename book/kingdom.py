col_a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
loc = input()
row = int(loc[1])
col = col_a[loc[0]]

cnt=0

go = [(1,2), (1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
for g in go:
    r = row + g[0]
    c = col + g[1]

    if r >= 1 and r<=8 and c >=1 and c<=8:
        cnt = cnt+1

print(cnt)