import sys
N, L = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
road = [[]] * L
light = []
# for i in range(N):
#     k = 1
#     while len(road[arr[i][0] - 1]) < 2 * L:
#         road[arr[i][0] - 1] = ([1] * arr[i][2] + [0] * arr[i][1])  * k
#         k += 1
for i in range(L):
    for j in range(N):
        if arr[j][0] == i:
            k = 1
            while len(road[arr[j][0] - 1]) < L ** 2:
                road[arr[j][0] - 1] = ([1] * arr[j][2] + [0] * arr[j][1])  * k
                k += 1
        else:
            road[i] = [1]
    
# print(road)
result = 0
for i in range(len(road)):
    tmp_arr = road[i]
    if len(tmp_arr) == 1:
        result += 1
        print('정상')
    else:
        tmp = result
        print(tmp)
        print(tmp_arr)
        for j in range(tmp):

            tmp_arr.pop()
        print(tmp_arr)
        if tmp_arr[-1] == 1:
            result += 1
            print('여기')
        else:
            while tmp_arr[-1] != 1:
                print('저기')
                tmp_arr.pop()
                result += 1
            
print(result)

