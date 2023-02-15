N = int(input())
go = input().split()
x, y = 1, 1

for g in go:
    if g == 'L':
        y = y - 1
        if y < 1:
            y = y + 1
    if g == 'R':
        y = y + 1
        if y > N:
            y = y - 1
    if g == 'U':
        x = x - 1
        if x < 1:
            x = x + 1
    if g == 'D':
        x = x + 1
        if x > N:
            x = x - 1

print(x, y)


