N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]


def get_bw(r1, r2, c1, c2):
    if r1 + 1 == r2:
        if arr[r1][c1] == 1:
            return (1, 0)
        else:
            return (0, 1)

    rmid = (r1 + r2) // 2
    cmid = (c1 + c2) // 2

    ret1 = get_bw(r1, rmid, c1, cmid)
    ret2 = get_bw(r1, rmid, cmid, c2)
    ret3 = get_bw(rmid, r2, c1, cmid)
    ret4 = get_bw(rmid, r2, cmid, c2)

    if ret1 == ret2 == ret3 == ret4:
        if ret1 == (1, 0):
            return (1, 0)
        elif ret1 == (0, 1):
            return (0, 1)
    return (
        ret1[0] + ret2[0] + ret3[0] + ret4[0],
        ret1[1] + ret2[1] + ret3[1] + ret4[1],
    )


ret = get_bw(0, N, 0, N)
print(ret[1])
print(ret[0])
