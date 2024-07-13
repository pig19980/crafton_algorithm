# 12:56 13:02
N = int(input())
E = int(input())

unions = list(range(N + 1))


def get_top(pos):
    if pos == unions[pos]:
        return pos
    top = get_top(unions[pos])
    unions[pos] = top
    return top


for _ in range(E):
    s, e = map(int, input().split(" "))
    s_top, e_top = get_top(s), get_top(e)

    if s_top != e_top:
        unions[s_top] = e_top

virus_top = get_top(1)

cnt = -1
for i in range(1, N + 1):
    i_top = get_top(i)
    if i_top == virus_top:
        cnt += 1

print(cnt)
