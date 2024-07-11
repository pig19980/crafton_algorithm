# 8:42


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if len(self.arr) == 0:
            return -1
        ret = self.arr[-1]
        self.arr.pop()
        return ret


N = int(input())
for _ in range(N):
    got = input()
    stack = Stack()
    passed = True
    for s in got:
        if s == "(":
            stack.push(1)
        else:
            poped = stack.pop()
            if poped == -1:
                passed = False
                break
    if len(stack.arr) != 0:
        passed = False
    if passed:
        print("YES")
    else:
        print("NO")
