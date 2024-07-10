import sys

input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.arr = []

    def empty(self):
        return len(self.arr) == 0

    def top(self):
        if self.empty():
            print("TOP EMPTY ERROR")
            exit()
        return self.arr[-1]

    def push(self, val1, val2):
        self.arr.append((val1, val2))
        return

    def pop(self):
        if self.empty():
            print("POP EMPTY ERROR")
            exit()
        ret = self.top()
        self.arr.pop()
        return ret


while True:
    got = input().split(" ")
    if len(got) == 1:
        break
    arr = list(map(int, got))
    N = arr[0]
    arr = arr[1:]

    maxA = 0
    stack = Stack()
    stack.push(0, -1)
    for ci, ch in enumerate(arr):
        if stack.empty():
            stack.push(ch, ci)
            continue

        put_idx = ci
        while not stack.empty():
            bh, bi = stack.top()
            if bh <= ch:
                break
            put_idx = bi

            stack.pop()
            curA = bh * (ci - bi)
            if curA > maxA:
                maxA = curA

        if bh != ch:
            stack.push(ch, put_idx)

    while not stack.empty():
        h, i = stack.pop()
        curA = h * (len(arr) - i)
        if curA > maxA:
            maxA = curA

    print(maxA)
