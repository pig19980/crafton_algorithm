# 10:19 10:23
N, M = map(int, input().split(" "))
A = set(map(int, input().split(" ")))
B = set(map(int, input().split(" ")))

print(len(A) + len(B) - 2 * (len(A & B)))
