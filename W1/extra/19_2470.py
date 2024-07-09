N = int(input())
liquids = sorted(list(map(int, input().split())))

# print(liquids)

l, r = 0, len(liquids) - 1

minAbs = 9876543210
mS, mB = None, None

while l != r:
    mixed = liquids[l] + liquids[r]
    if abs(mixed) < minAbs:
        mS = liquids[l]
        mB = liquids[r]
        minAbs = abs(mixed)

    if mixed < 0:
        l += 1
    else:
        r -= 1

print(mS, mB)
