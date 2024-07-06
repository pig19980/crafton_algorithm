N = int(input())
arr = list(map(int, input().split(" ")))

if N == 1:
    print(0)
    exit()

next_max = [-1] * N


def get_next_high_idx(idx, h):
    # print(idx, h)
    if idx == -1:
        return -1
    if arr[idx] > h:
        return idx
    return get_next_high_idx(next_max[idx], h)


for idx in range(1, N):
    next_max[idx] = get_next_high_idx(idx - 1, arr[idx])

# print(next_max)
for elem in next_max:
    print(f"{elem + 1} ", end="")
print()
