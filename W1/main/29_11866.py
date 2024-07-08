N, gap = map(int, input().split(" "))

init_arr = list(range(1, N + 1))
ret_arr = []

idx = -1
while len(init_arr) != 0:
    idx = (idx + gap) % len(init_arr)
    ret_arr.append(init_arr[idx])
    init_arr.pop(idx)
    idx -= 1
# print(ret_arr)

print("<", end="")
for elem in ret_arr[:-1]:
    print(f"{elem}, ", end="")
print(f"{ret_arr[-1]}>")
