import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
road = [1] * L
for i in range(N):
    road[arr[i][0] - 1] = [arr[i][1], arr[i][2], arr[i][1] + arr[i][2]]
time = 0
for i in range(len(road)):
    if road[i] == 1:
        time += 1
        print(time)
    else:
        tmp = time
        print(f'time은 {time}, i는 {i}')
        while tmp > road[i][2]:
            tmp = tmp - road[i][2]
            
        if tmp > road[i][0]:
            print(f'if : tmp = {tmp} road[i] = {road[i]}')
            time += 1
            print(time)
        else:
            print(f'else: tmp = {tmp} road[i] = {road[i]}')

            time += (road[i][0] - tmp + 1)
            print(time)
print(time)