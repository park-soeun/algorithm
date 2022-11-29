import sys
N = int(sys.stdin.readline().rstrip())
arr = [[0] * (N + 2)]
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    tmp = [0] + tmp + [0]
    arr.append(tmp)
arr.append([0] * (N + 2))
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = []
tmp_num = 1
cnt = 0
for i in range(N + 1):
    for j in range(N + 1):
        if arr[i][j] != 0:
            tmp_num += 1
            while ans:
                for d in range(4):
                    ni = i + dir[d][0]
                    nj = j + dir[d][1]
                    if arr[ni][nj] != 0:
                        cnt += 1
                        arr[ni][nj] = 2
                    else:
                        ans = false
        result.append(cnt)
print(result)

        # if arr[i][j] == tmp_num:
        #     arr[i][j] = tmp_num + 1
        # if arr[i][j] == tmp_num + 1:

            

