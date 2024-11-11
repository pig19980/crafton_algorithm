# 10:37 10:42
N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

A.extend(B)
A.sort()

for a in A:
    print(a, end=" ")
print()
