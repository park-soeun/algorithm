import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 포문으로 해당값 대입하기
road = [[]] * L
light = []
print(road)
for i in range(N):
#     # light.append([0] * arr[i][1] + [1] * arr[i][2])
#     # ? 여기 -1 맞는지 확인

    k = 1
    while len(road[arr[i][0] - 1]) < L:
        road[arr[i][0] - 1] = ([1] * arr[i][2] + [0] * arr[i][1]) * k
        k += 1
    
    
print(road)
result = 0
for i in range(len(road)):
    if road[i][-1] == 1:
        continue
    else:
        tmp = result
        # while tmp > len(road[i]):
        #     tmp - len(road[i])
        # else:
        #     print(tmp, road[i])
        k = 1
        while len(road[i]) < L:
            road[i] += road[i]
