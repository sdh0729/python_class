n, m = map(int, input().split())

x , y, d = map(int, input().split())

ewsn = [0, 1, 2, 3]
pd = [x,y]
a=[]
for i in range(n):
	a.append(list(map(int, input().split())))

cnt = 1

def turning():
