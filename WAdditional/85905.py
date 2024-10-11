# 10:28 10:37
N = int(input())
got = input()

digit = {}
for i in range(10):
    digit[str(i)] = i

Sum, idx = 0, 0
while idx < len(got):
    tempSum = 0
    if got[idx] in digit:
        while idx < len(got) and got[idx] in digit:
            tempSum *= 10
            tempSum += digit[got[idx]]
            idx += 1
        Sum += tempSum
    else:
        idx += 1

print(Sum)
