# 10:08
import sys

input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split(" "))
fire_map = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split(" "))
    fire_map[r][c].append((m, s, d))

for _ in range(K):
    new_fire_map = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            for fm, fs, fd in fire_map[r][c]:
                nr, nc = r + dr[fd] * fs, c + dc[fd] * fs
                while nr < 1:
                    nr += N
                while nc < 1:
                    nc += N
                while nr > N:
                    nr -= N
                while nc > N:
                    nc -= N
                new_fire_map[nr][nc].append((fm, fs, fd))

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            fires = new_fire_map[r][c]
            if len(fires) in [0, 1]:
                continue
            all_even_or_odd = True
            sum_mass = 0
            sum_speed = 0
            for idx in range(len(fires)):
                sum_mass += fires[idx][0]
                sum_speed += fires[idx][1]
                if all_even_or_odd and fires[idx - 1][2] % 2 != fires[idx][2] % 2:
                    all_even_or_odd = False
            new_mass = sum_mass // 5
            new_speed = sum_speed // len(fires)
            new_fire_map[r][c] = []
            if new_mass == 0:
                continue
            if all_even_or_odd:
                new_dirs = [0, 2, 4, 6]
            else:
                new_dirs = [1, 3, 5, 7]
            for new_dir in new_dirs:
                new_fire_map[r][c].append((new_mass, new_speed, new_dir))

    fire_map, new_fire_map = new_fire_map, fire_map

mass_sum = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        for fire in fire_map[r][c]:
            mass_sum += fire[0]

print(mass_sum)
