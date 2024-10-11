# 10:18 10:28
N = input()
digit = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
for i in range(10):
    digit[str(i)] = i

S = 0
if N[0] == "0":
    if N[1] == "x":
        idx = 2
        mul = 16
    else:
        idx = 1
        mul = 8
else:
    idx = 0
    mul = 10

for n in N[idx:]:
    S *= mul
    S += digit[n]

print(S)
