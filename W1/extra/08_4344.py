N = int(input())
for _ in range(N):
    gotline = list(map(int, input().split(" ")))
    scores = gotline[1:]
    mid = sum(scores) / len(scores)
    cnt = 0
    for s in scores:
        if s > mid:
            cnt += 1
    print(f"{cnt / len(scores):.3%}")
