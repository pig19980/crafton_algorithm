from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
oper = []
min_ans = int(1e8)
max_ans = -int(1e8)

for i, o in zip(list(map(int, input().split())), ["+", "-", "*", "/"]):
    for j in range(i):
        oper.append(o)


for opers in set(permutations(oper, len(oper))):
    cnt = num[0]

    for i, o in enumerate(opers):
        if o == "+":
            cnt += num[i + 1]
        elif o == "-":
            cnt -= num[i + 1]
        elif o == "*":
            cnt *= num[i + 1]
        elif o == "/":
            if cnt < 0:
                cnt = -cnt // num[i + 1]
                cnt *= -1
            else:
                cnt //= num[i + 1]

    min_ans = min(min_ans, cnt)
    max_ans = max(max_ans, cnt)

print(max_ans)
print(min_ans)
