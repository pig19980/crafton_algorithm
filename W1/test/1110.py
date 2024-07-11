initN = list(map(int, list(input())))
if len(initN) == 1:
    initN = [0] + initN
# print(initN)

curN = initN.copy()
cnt = 0
while True:
    cnt += 1
    sum = (curN[0] + curN[1]) % 10
    curN = [curN[1]] + [sum]
    # print(curN)

    if initN == curN:
        break

print(cnt)
