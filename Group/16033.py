# 3:03 4:02
import sys

input = sys.stdin.readline

while True:
    n, m, t, p = map(int, input().split(" "))
    if (n, m, t, p) == (0, 0, 0, 0):
        break
    paper_map = [[1 for _ in range(n)] for _ in range(m)]
    x_start, y_start = 0, 0
    x_end, y_end = n, m
    for _ in range(t):
        d, c = map(int, input().split(" "))
        if d == 1:
            if 2 * c <= x_end - x_start:
                new_x_start = x_start + c
                for y in range(y_start, y_end):
                    for dx in range(c):
                        paper_map[y][new_x_start + c - dx - 1] += paper_map[y][x_start + dx]
                x_start = new_x_start
            else:
                new_x_end = x_start + c
                for y in range(y_start, y_end):
                    for dx in range(x_end - x_start - c):
                        paper_map[y][new_x_end - dx - 1] += paper_map[y][new_x_end + dx]
                    for dx in range((new_x_end - x_start) // 2):
                        (paper_map[y][x_start + dx], paper_map[y][new_x_end - dx - 1]) = (
                            paper_map[y][new_x_end - dx - 1],
                            paper_map[y][x_start + dx],
                        )
                x_end = new_x_end
        else:
            if 2 * c <= y_end - y_start:
                new_y_start = y_start + c
                for x in range(x_start, x_end):
                    for dy in range(c):
                        paper_map[new_y_start + c - dy - 1][x] += paper_map[y_start + dy][x]
                y_start = new_y_start
            else:
                new_y_end = y_start + c
                for x in range(x_start, x_end):
                    for dy in range(y_end - y_start - c):
                        paper_map[new_y_end - dy - 1][x] += paper_map[new_y_end + dy][x]
                    for dy in range((new_y_end - y_start) // 2):
                        (paper_map[y_start + dy][x], paper_map[new_y_end - dy - 1][x]) = (
                            paper_map[new_y_end - dy - 1][x],
                            paper_map[y_start + dy][x],
                        )
                y_end = new_y_end
    for _ in range(p):
        x, y = map(int, input().split(" "))
        print(paper_map[y_start + y][x_start + x])
