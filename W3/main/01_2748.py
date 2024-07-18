# 10:44 10:49

N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    num0 = 0
    num1 = 1
    curidx = 1
    while curidx < N:
        num0, num1 = num1, num0 + num1
        curidx += 1
    print(num1)
