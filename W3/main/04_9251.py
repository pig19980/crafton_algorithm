# 12:11 12:30

s1, s2 = input(), input()
costs = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

for i2 in range(len(s2)):
    for i1 in range(len(s1)):
        if s1[i1] == s2[i2]:
            costs[i2 + 1][i1 + 1] = costs[i2][i1] + 1
        else:
            costs[i2 + 1][i1 + 1] = max(costs[i2 + 1][i1], costs[i2][i1 + 1])

print(costs[len(s2)][len(s1)])
