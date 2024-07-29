# 2:09
import sys
from collections import deque

input = sys.stdin.readline


def cmdD(num):
    return num * 2 % 10000


def cmdS(num):
    return (num + 9999) % 10000


def cmdL(num):
    front = num // 1000
    return (num - front * 1000) * 10 + front


def cmdR(num):
    end = num % 10
    return end * 1000 + num // 10


cmdFuntions = [cmdD, cmdS, cmdL, cmdR]
cmds = ["D", "S", "L", "R"]

T = int(input())
for _ in range(T):
    got, obj = map(int, input().split(" "))
    costs = [None for _ in range(10001)]
    costs[got] = ""
    nexts = deque()
    nexts.append(got)

    while nexts:
        cur = nexts.popleft()
        if cur == obj:
            break
        for i in range(4):
            next_ = cmdFuntions[i](cur)
            if costs[next_] == None:
                costs[next_] = costs[cur] + cmds[i]
                if next_ == obj:
                    break
                nexts.append(next_)
        if next_ == obj:
            break

    print(costs[obj])
