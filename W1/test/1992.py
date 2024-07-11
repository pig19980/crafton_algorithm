N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))

dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]


def get_tree(row, col, size):
    if size == 1:
        return str(arr[row][col])

    size = size // 2

    child_ret = []
    for i in range(4):
        child_ret.append(get_tree(row + dy[i] * size, col + dx[i] * size, size))

    # print(child_ret)
    canCompress = True
    val = child_ret[0]
    for i in range(4):
        if len(child_ret[i]) == 1 and val == child_ret[i]:
            continue
        canCompress = False
        break
    if canCompress:
        return val
    else:
        ret = "("
        for i in range(4):
            ret += child_ret[i]
        ret += ")"
        return ret


print(get_tree(0, 0, N))
