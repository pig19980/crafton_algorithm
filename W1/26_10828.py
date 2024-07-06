import sys

input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    gotline = input()
    if " " in gotline:
        cmd, val = gotline.split(" ")
        val = int(val)
    else:
        cmd = gotline.rstrip("\n")

    if cmd == "push":
        stack.append(val)
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    # print(stack)
