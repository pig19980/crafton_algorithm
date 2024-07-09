N = int(input())
for _ in range(N):
    got = input()
    rec, score = 0, 0
    for c in got:
        if c == "O":
            rec += 1
            score += rec
        else:
            rec = 0
    print(score)
