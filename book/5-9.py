from collections import deque

def a(g, s, v):
    queue = deque([s])
    v[s] = True
    while queue:
        vi= queue.popleft()
        print(vi, end = '')
        for i in g[vi]:
            if not v[i]:
                queue.append(i)
                v[i]=True

g = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

v = [False] * 9
a(g,1,v)