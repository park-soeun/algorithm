import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 포문으로 해당값 대입하기
road = [[]] * L
light = []
# print(road)
for i in range(N):
#     # light.append([0] * arr[i][1] + [1] * arr[i][2])
#     # ? 여기 -1 맞는지 확인

    k = 1
    while len(road[arr[i][0] - 1]) < L + 1:
        road[arr[i][0] - 1] = ([1] * arr[i][2] + [0] * arr[i][1])  * k
        k += 1
for i in range(L):
    # print(len(road[i]))
    if len(road[i]) == 0:
        road[i] = [1]
    
    
# print(road)
result = 0
for i in range(len(road)):
    if road[i][-1] == 1 and len(road[i]) == 1:
        result += 1
    else:
        # print(road[i])
        # print
        tmp = result
        
        for j in range(tmp):
            road[i].pop()
        if road[i][-1] == 1:
            result += 1
        else:
            while road[i][-1] != 1:
                road[i].pop()
                result += 1
print(result)

