# 32 min
N = int(input())
arr = list(map(int, input().split(" ")))
INF = 98765


def get_ab(idx):
    if arr[idx] == arr[idx + 1]:
        if arr[idx] == arr[idx + 2]:
            return 0, arr[idx]
        else:
            return INF, INF
    b = (arr[idx + 1] ** 2 - arr[idx] * arr[idx + 2]) // (arr[idx + 1] - arr[idx])
    if arr[idx] != 0:
        a = (arr[idx + 1] - b) // arr[idx]
    else:
        a = (arr[idx + 2] - b) // arr[idx + 1]

    if arr[idx + 2] != a * arr[idx + 1] + b or arr[idx + 1] != a * arr[idx] + b:
        return INF, INF
    else:
        return a, b


if N >= 3:
    first_ab = get_ab(0)
    check_ok = True
    for i in range(N - 2):
        cur_ab = get_ab(i)
        if first_ab != cur_ab or cur_ab == (INF, INF):
            check_ok = False
            break
    if not check_ok:
        print("B")
    else:
        print(first_ab[0] * arr[-1] + first_ab[1])
elif N == 2:
    if arr[0] != arr[1]:
        print("A")
    else:
        print(arr[0])
else:
    print("A")
