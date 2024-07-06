N, B = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr[i][j] %= 1000


def printMat(mat):
    for row in mat:
        for elem in row:
            print(f"{elem} ", end="")
        print()


def getMultIJ(matA, matB, i, j):
    sum = 0
    for k in range(N):
        sum += matA[i][k] * matB[k][j]
    return sum % 1000


def MultMat(matA, matB):
    return [[getMultIJ(matA, matB, i, j) for j in range(N)] for i in range(N)]


def get_power(mult):
    # print(mult)
    if mult == 1:
        return arr
    ret = get_power(mult // 2)
    ret = MultMat(ret, ret)
    if mult % 2 == 1:
        ret = MultMat(ret, arr)
    return ret


printMat(get_power(B))
