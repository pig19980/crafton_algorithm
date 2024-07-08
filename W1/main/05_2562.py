max = -1
row = -1
for i in range(9):
    got = int(input())
    if got > max:
        max = got
        row = i + 1
print(max)
print(row)
