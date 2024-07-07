import sys

input = sys.stdin.readline

N = int(input())


class Queue:
    def __init__(self):
        self.arr = []
        self.idx = 0

    def size(self):
        return len(self.arr) - self.idx

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.arr[self.idx]

    def back(self):
        if self.size() == 0:
            return -1
        return self.arr[-1]

    def push(self, X):
        self.arr.append(X)

    def pop(self):
        if self.size() == 0:
            return -1
        ret = self.front()
        self.idx += 1
        return ret


queue = Queue()

for _ in range(N):
    gotline = input()
    if " " in gotline:
        cmd, val = gotline.split(" ")
        val = int(val)
    else:
        cmd = gotline.rstrip("\n")

    if cmd == "push":
        queue.push(val)
    elif cmd == "pop":
        print(queue.pop())
    elif cmd == "size":
        print(queue.size())
    elif cmd == "empty":
        print(queue.empty())
    elif cmd == "front":
        print(queue.front())
    elif cmd == "back":
        print(queue.back())
