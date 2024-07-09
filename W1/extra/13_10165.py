def check(num):
    arr = list(map(int, list(str(num))))
    if len(arr) == 1:
        return True
    gap = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] != gap:
            return False
    return True


got = int(input())
cnt = 0
for i in range(1, got + 1):
    if check(i):
        cnt += 1
print(cnt)
