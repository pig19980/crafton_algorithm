height = [0] * 9
for i in range(9):
    height[i] = int(input())
height.sort()

hsum = sum(height)
for i in range(9):
    for j in range(i + 1, 9):
        if hsum - height[i] - height[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(height[k])

            exit()
