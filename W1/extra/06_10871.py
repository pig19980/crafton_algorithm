N, X = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

ret = ""
for elem in arr:
    if elem < X:
        ret += f"{elem} "
print(ret)
