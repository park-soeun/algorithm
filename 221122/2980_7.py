import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
road = [[]] * L
light = []
for i in range(L):
    for j in range(N):
        if arr[j][0] == i:
            k = 1
            while len(road[arr[j][0] - 1]) < L * 10:
                road[arr[j][0] - 1] = ([1] * arr[j][2] + [0] * arr[j][1])  * k
                k += 1
        else:
            road[i] = [1]
    
result = 0
for i in range(len(road)):
    tmp_arr = road[i]
    if len(tmp_arr) == 1:
        result += 1
    else:
        tmp = result
        for j in range(tmp):
            tmp_arr.pop()
        if tmp_arr[-1] == 1:
            result += 1
        else:
            while tmp_arr[-1] != 1:
                tmp_arr.pop()
                result += 1
            
print(result)

