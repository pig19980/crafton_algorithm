import sys

input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    cn, cs, ce = map(int, input().split(" "))
    classes.append((cn - 1, cs, ce))

classes.sort(key=lambda x: -x[1])

given_room = [None for _ in range(N)]
running_room = []
max_running = 0

while classes:
    cn, cs, ce = classes.pop()
    room_found = False
    for i in range(len(running_room)):
        if running_room[i] <= cs:
            given_room[cn] = i + 1
            running_room[i] = ce
            room_found = True
            break
    if room_found:
        continue
    running_room.append(ce)
    given_room[cn] = len(running_room)
    if max_running < len(running_room):
        max_running = len(running_room)

print(max_running)
for room in given_room:
    print(room)
