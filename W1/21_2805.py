N, M = map(int, input().split(" "))
treeHs = list(map(int, input().split(" ")))

mh, Mh = 0, 1000000001


def check_ok(ch):
    sum = 0
    for treeH in treeHs:
        if treeH > ch:
            sum += treeH - ch
    if sum >= M:
        return True
    else:
        return False


while True:
    # print(mh, Mh)
    ch = (mh + Mh) // 2
    if check_ok(ch):
        mh = ch
    else:
        Mh = ch

    if mh + 1 == Mh:
        break


print(mh)
