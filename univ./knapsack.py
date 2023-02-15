from copy import deepcopy

def promising(i: int, profit: int, weight: int) -> bool:
    global bound, totweight

    if weight >= W:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight

        while j <= n and totweight + w[j] <= W:

            totweight += w[j]
            bound += p[j]
            j += 1

        k = j
        if k <= n:
            bound += (W - totweight) * (p[k] // w[k])

        return bound > maxprofit


def func(i: int, profit: int, weight: int) -> None:
    global maxprofit, bestset
    if weight <= W and profit >= maxprofit:
        maxprofit = profit
        bestset = deepcopy(include)

    flag = promising(i, profit, weight)

    if flag:
        include[i + 1] = True
        func(i + 1, profit + p[i + 1], weight + w[i + 1])

        include[i + 1] = False
        func(i + 1, profit, weight)


n, W = map(int, input().split())
w = list(map(int, input().split()))
p = list(map(int, input().split()))

item = [(i, j) for i, j in zip(w, p)]
item = [(0, 0)] + list(sorted(item, key=lambda x: x[1] // x[0], reverse=True))
w, p = zip(*item)

maxprofit = 0
include = [0] * (n + 1)
bestset = [0] * (n + 1)
totweight = 0
bound = 0

func(0, 0, 0)

print(maxprofit)


