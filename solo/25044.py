# 10:00 10:44
N, K = map(int, input().split(" "))


class clock:
    def __init__(self, hh, mm):
        self.day = 0
        self.hh = hh
        self.mm = mm

    def next_day(self, kmin):
        self.mm += kmin
        if self.mm >= 60:
            self.hh += 1
            self.mm %= 60
        if self.hh >= 24:
            self.day += 1
            self.hh %= 24
        self.day += 1

    def __lt__(self, other: "clock"):
        if self.hh == other.hh:
            return self.mm < other.mm
        return self.hh < other.hh

    def __repr__(self) -> str:
        return f"{self.hh:02}:{self.mm:02}"


clock1 = clock(15, 0)
clock2 = clock(18, 0)
clock3 = clock(21, 0)

while clock1.day < N:
    clock1.next_day(K)
    # print(clock1)
while clock2.day < N:
    clock2.next_day(K)
while clock3.day < N:
    clock3.next_day(K)

clocks = []
if clock1.day == N:
    clocks.append(clock1)
if clock2.day == N:
    clocks.append(clock2)
if clock3.day == N:
    clocks.append(clock3)

clocks.sort()
print(len(clocks))
for c in clocks:
    print(c)
