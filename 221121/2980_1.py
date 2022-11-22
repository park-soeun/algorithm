import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
road = [1] * L
for i in range(N):
    road[arr[i][0] - 1] = [arr[i][1], arr[i][2], arr[i][1] + arr[i][2]]
time = 0
print(road)
for i in range(len(road)):
    if road[i] == 1:
        time += 1
    else:
        tmp = time
        print(tmp, road[i][2], time)
        while tmp > road[i][2]:
            print('while')
            tmp = tmp - road[i][2]
            
        
        if tmp >= road[i][0]:
            print('여기')
            time += 1
            
        else:
            print('저기')
            print(time, road[i], tmp)
            time += (road[i][0] - tmp)
            
            
print(time)