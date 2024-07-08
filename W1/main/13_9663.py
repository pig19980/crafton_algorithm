N = int(input())

q_loc = [0] * N
cnt = 0


flag_1 = [False] * N
flag_2 = [False] * (N * 2 - 1)
flag_3 = [False] * (N * 2 - 1)


def check_board(M):
    global cnt
    if M == N:
        cnt += 1
        return
    for i in range(N):
        if flag_1[i]:
            continue
        if flag_2[i + M]:
            continue
        if flag_3[N - i + M - 1]:
            continue
        q_loc[M] = i

        flag_1[i] = True
        flag_2[i + M] = True
        flag_3[N - i + M - 1] = True
        q_loc[M] = i

        check_board(M + 1)

        flag_1[i] = False
        flag_2[i + M] = False
        flag_3[N - i + M - 1] = False


check_board(0)

print(cnt)
