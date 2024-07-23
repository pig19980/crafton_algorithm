# 2:27 2:47

N, K = map(int, input().split(" "))
nexts = list(map(int, input().split(" ")))

plugs = []
cnt = 0

for i in range(K):
    if nexts[i] in plugs:
        continue
    if len(plugs) < N:
        plugs.append(nexts[i])
        continue
    change_idx = 0
    max_come = -1
    for j in range(N):
        # check when it come
        k = i
        while k < K:
            if nexts[k] == plugs[j]:
                break
            k += 1
        if max_come < k:
            change_idx = j
            max_come = k
    plugs[change_idx] = nexts[i]
    cnt += 1

print(cnt)
