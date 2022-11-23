# 가로로 바꾸면 세로만 검사
# 세로로 바꾸면 가로만 검사

import sys
num = int(sys.stdin.readline().rstrip())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(num)]
result = 0
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0
for i in range(num):
    for j in range(num):
        while d < 4:
            ni = i
            nj = j
            conv_i = ni + dir[d][0]
            conv_j = nj + dir[d][1]
            if arr[conv_i] and arr[conv_j]:
                arr[ni], arr[conv_i] = arr[conv_i], arr[ni]
            


print(arr)
