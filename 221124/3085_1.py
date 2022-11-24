# 가로로 바꾸면 세로만 검사
# 세로로 바꾸면 가로만 검사

import sys
import copy
num = int(sys.stdin.readline().rstrip())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(num)]
result = 0
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0
result = []

for i in range(num):
    for j in range(num):
        ni = i
        nj = j
        for k in range(4):
            tmp = copy.deepcopy(arr)
            conv_i = ni + dir[k][0]
            conv_j = nj + dir[k][1]
            # print(ni, nj, conv_i, conv_j)
            if 0 <= conv_i < num and 0 <= conv_j < num:
                if arr[ni][nj] != arr[conv_i][conv_j]:
                    tmp[ni][nj] = arr[conv_i][conv_j]
                    tmp[conv_i][conv_j] = arr[ni][nj]
                    # arr[ni][nj], arr[conv_i][conv_j] = arr[conv_i][conv_j], arr[ni][nj]
                    if tmp not in result:
                        result.append(tmp)
            

# for ele in range(len(result)):
#     for i in range(num):
        
#         print(result[ele][i])
    
#     print()
# # 가로, 세로
final_result = []
for ele in range(len(result)):
    for i in range(num):
        first_1 = result[ele][i][0]
        first_2 = result[ele][0][i]
        cnt1 = 1
        cnt2 = 1
        for j in range(1, num):
            if first_1 == result[ele][i][j]:
                cnt1 += 1
            if first_2 == result[ele][j][i]:
                cnt2 += 1
            final_result.append(cnt1)
            final_result.append(cnt2)
     
print(max(final_result))
  # for ele in range(len(result)):
#     for i in range(num):
#         for j in range(num):
#             result[ele][i]
                



