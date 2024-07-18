# 10:51 11:06

N = int(input())

if N == 1:
    print(1)
else:
    num0 = 1
    num1 = 2
    for idx in range(2, N):
        num1, num0 = (num1 + num0) % 15746, num1
    print(num1)
