N = int(input())
nodes = dict()

for _ in range(N):
    key, l, r = input().split(" ")
    nodes[key] = [l, r]
# print(nodes)


def junwe(cur):
    if cur == ".":
        return ""
    return cur + junwe(nodes[cur][0]) + junwe(nodes[cur][1])


def jungwe(cur):
    if cur == ".":
        return ""
    return jungwe(nodes[cur][0]) + cur + jungwe(nodes[cur][1])


def huwe(cur):
    if cur == ".":
        return ""
    return huwe(nodes[cur][0]) + huwe(nodes[cur][1]) + cur


print(junwe("A"))
print(jungwe("A"))
print(huwe("A"))
