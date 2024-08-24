# 45min
import sys

input = sys.stdin.readline

N = int(input())
wines = []
for _ in range(N):
    wines.append(int(input()))

cur_drink = [0 for _ in range(N)]
cur_not_drink = [0 for _ in range(N)]

cur_drink[0] = wines[0]

for i in range(1, N):
    if i == 1:
        cur_drink[1] = wines[1] + wines[0]
    if i - 1 >= 0:
        cur_drink[i] = max(cur_drink[i], wines[i] + cur_not_drink[i - 1])
    if i - 2 >= 0:
        cur_drink[i] = max(cur_drink[i], wines[i] + wines[i - 1] + cur_not_drink[i - 2])
    cur_not_drink[i] = max(cur_not_drink[i - 1], cur_drink[i - 1])

# print(cur_drink)
# print(cur_not_drink)
print(max(cur_drink))
