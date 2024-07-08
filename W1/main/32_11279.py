class pQueue:
    def __init__(self):
        self.arr = [None]
        self.isEmpty = True

    def downHeap(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        # print("cur", idx, self.arr)
        if left > len(self.arr) - 1:
            return
        if right > len(self.arr) - 1:
            if self.arr[idx] < self.arr[left]:
                self.arr[idx], self.arr[left] = self.arr[left], self.arr[idx]
            return

        next = idx

        if self.arr[next] < self.arr[left]:
            next = left
        if self.arr[next] < self.arr[right]:
            next = right

        if next == idx:
            return
        else:
            self.arr[idx], self.arr[next] = self.arr[next], self.arr[idx]
            self.downHeap(next)

    def upHeap(self, idx):
        if idx == 1:
            return
        parent = idx // 2
        if self.arr[parent] < self.arr[idx]:
            self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
            self.upHeap(parent)

    def put(self, val):
        if self.isEmpty:
            self.arr.append(val)
            self.isEmpty = False
            return

        self.arr.append(val)
        self.upHeap(len(self.arr) - 1)

    def get(self):
        if self.isEmpty:
            return 0
        ret = self.arr[1]
        self.arr[1] = self.arr[-1]
        self.arr.pop()
        self.downHeap(1)

        if len(self.arr) == 1:
            self.isEmpty = True
        return ret


pq = pQueue()
# inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in inputs:
#     pq.put(i)
# while not pq.isEmpty:
#     print(pq.get())

import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    got = int(input())
    if got == 0:
        print(pq.get())
    else:
        pq.put(got)
    # print(got, pq.arr)
