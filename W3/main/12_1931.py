# 10:01 10:10
import sys

input = sys.stdin.readline

N = int(input())
time_table = []
for _ in range(N):
    s, e = map(int, input().split(" "))
    time_table.append((s, e))

time_table.sort(key=lambda x: (-x[1], -x[0]))

cnt = 0
before_e = -1
while time_table:
    while time_table and time_table[-1][0] < before_e:
        time_table.pop()
    if not time_table:
        continue
    s, e = time_table.pop()
    cnt += 1
    before_e = e

print(cnt)
