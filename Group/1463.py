from collections import deque


def op1(x):
    if x % 3 != 0:
        return x
    return x // 3


def op2(x):
    if x % 2 != 0:
        return x
    return x // 2


def op3(x):
    if x < 1:
        return x
    return x - 1


ops = [op1, op2, op3]
costs = [None for _ in range(1000001)]

got = int(input())
costs[got] = 0
q = deque([got])
while q:
    cur = q.popleft()
    if cur == 1:
        break
    for op in ops:
        next = op(cur)
        if costs[next] == None:
            costs[next] = costs[cur] + 1
            q.append(next)
print(costs[1])
