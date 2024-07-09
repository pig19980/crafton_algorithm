context = list(input().split(" "))
ret = len(context)
if context[0] == "":
    ret -= 1
if context[-1] == "":
    ret -= 1
print(ret)
