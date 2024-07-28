def get_elem(s1, s2, idx):
    if idx < len(s1):
        return s1[idx]
    elif idx == len(s1):
        return "#"
    elif idx < len(s1) + len(s2) + 1:
        return s2[idx - len(s1) - 1]
    elif idx == len(s1) + len(s2) + 1:
        return "$"
    else:
        return "\0"


# build suffix array with Manber-Myers Algorithm
def build_suffs(s1, s2):
    totL = len(s1) + len(s2) + 2
    suffs = list(range(totL))
    ranks = [ord(get_elem(s1, s2, i)) for i in range(totL)]
    nranks = [None for _ in range(totL)]
    depth = 1

    def get_rank(idx):
        if idx < totL:
            return ranks[idx]
        else:
            return 0

    while depth < totL:
        key = lambda idx: (get_rank(idx), get_rank(idx + depth))
        suffs.sort(key=key)
        nranks[suffs[0]] = 1
        for i in range(1, totL):
            nranks[suffs[i]] = nranks[suffs[i - 1]] + (
                1 - (key(suffs[i - 1]) == key(suffs[i]))
            )
        ranks, nranks = nranks, ranks
        depth <<= 1

    return suffs


# In suffix array, before part is the most overlapping one
# because suffix array is sorted
# With this fact, we can check most overlapping one of starting with Some index.
# Also, if we find maximum overlappling one starting with Some index,
# maximum overlappling one starting with Next index will bigger than Max[Some index] - 1
# so we can search in less time
def find_lcs(s1, s2, suffs):
    totL = len(s1) + len(s2) + 2
    invsuffs = [None for _ in range(totL)]
    for i in range(totL):
        invsuffs[suffs[i]] = i

    totmax, curmax = 0, 0
    maxidx = 0

    for i in range(totL):
        s1idx, s2idx = i, suffs[invsuffs[i] - 1]
        while True:
            if (
                s1idx + curmax < totL
                and s2idx + curmax < totL
                and get_elem(s1, s2, s1idx + curmax) == get_elem(s1, s2, s2idx + curmax)
            ):
                curmax += 1
            else:
                break

        if (
            (s1idx < len(s1) and s2idx > len(s1))
            or (s1idx > len(s1) and s2idx < len(s1))
        ) and curmax > totmax:
            totmax = curmax
            maxidx = min(s1idx, s2idx)

        curmax = max(0, curmax - 1)

    return s1[maxidx : maxidx + totmax]


s1, s2 = input(), input()
if len(s1) > len(s2):
    s1, s2 = s2, s1
suffs = build_suffs(s1, s2)


max_overlapping = find_lcs(s1, s2, suffs)
print(len(max_overlapping))
print(max_overlapping)
