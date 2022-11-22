import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
road = [1] * L
for i in range(N):
    road[arr[i][0] - 1] = [arr[i][1], arr[i][2], arr[i][1] + arr[i][2]]
time = 0
i = 0
while i < L:
    print(f'i is {i}')
    if road[i] == 1:
        time += 1
        print(time)
        i += 1
    else:
        tmp = time
        print(f'time은 {time}, i는 {i}')
        while tmp > road[i][2]:
            tmp = tmp - road[i][2]
            
        if tmp >= road[i][0]:
            print(f'if : tmp = {tmp} road[i] = {road[i]}')
            time += 1
            i += 1
            print(time)
        else:
            print(f'else: tmp = {tmp} road[i] = {road[i]}')
            print(f' 이거 더해줌 {road[i][0] - tmp}')

            time += (road[i][0] - tmp )
            i += 1
            print(time)
print(time)