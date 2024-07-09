W, H = map(int, input().split(" "))
N = int(input())

Wcut = []
Hcut = []
for _ in range(N):
    cmd, idx = map(int, input().split(" "))
    if cmd == 0:
        Hcut.append(idx)
    else:
        Wcut.append(idx)

Wcut.sort()
Hcut.sort()

# print(W, H)
# print(Wcut, Hcut)

Wcutted = []
Hcutted = []

for i in range(len(Wcut)):
    if i == 0:
        Wcutted.append(Wcut[i])
        before = Wcut[0]
    else:
        Wcutted.append(Wcut[i] - before)
        before = Wcut[i]
    if i == len(Wcut) - 1:
        Wcutted.append(W - Wcut[i])

for i in range(len(Hcut)):
    if i == 0:
        Hcutted.append(Hcut[i])
        before = Hcut[0]
    else:
        Hcutted.append(Hcut[i] - before)
        before = Hcut[i]
    if i == len(Hcut) - 1:
        Hcutted.append(H - Hcut[i])

if len(Wcut) == 0:
    Wcutted.append(W)
if len(Hcut) == 0:
    Hcutted.append(H)

# print(Wcutted, Hcutted)


max = -1
for wpice in Wcutted:
    for hpice in Hcutted:
        if wpice * hpice > max:
            max = wpice * hpice

print(max)
