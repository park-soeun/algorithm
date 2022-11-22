import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
road = [1] * L
for i in range(N):
    road[arr[i][0] - 1] = [arr[i][1], arr[i][2], arr[i][1] + arr[i][2]]
time = 0
i = 0
while i < L:
    if road[i] == 1:
        time += 1
        i += 1
    else:
        tmp = time
        while tmp > road[i][2]:
            tmp = tmp - road[i][2]
        if tmp > road[i][0]:
            print(tmp, road[i])
            time += 1
            i += 1
        else:
            time += (road[i][0] - tmp)
            i += 1
print(time)