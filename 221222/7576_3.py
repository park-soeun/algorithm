def bfs(arr, arr2):
    for k in range(len(arr2)):
        q = []
        q.append(arr2[k])
        
        while q:
            tmp = q.pop(0)
            si = tmp[0]
            sj = tmp[1]
            for di, dj in ([0, -1], [-1, 0], [0, 1], [1, 0]):
                ni = si + di
                nj = sj + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = arr[si][sj] + 1
                        q.append([ni, nj])
                        si, sj = ni, nj
                    else:
                        if arr[ni][nj] > arr[si][sj] + 1:
                            arr[ni][nj] = arr[si][sj] + 1
                            q.append([ni, nj])
                            break
    return arr

import sys
M, N = map(int, sys.stdin.readline().rstrip().split())
list1 = []
tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            list1.append([i, j])


# dfs 하고 나서 arr 다시 뱉어서 0 검사해서 0 있으면 -1 출력 없으면 최대 숫자 출력
maxV = 0
ans1 = 0
ans2 = 0
after_tomato = bfs(tomato, list1)
print(after_tomato)
for i in range(N):
    for j in range(M):
        if after_tomato[i][j] == 0:
            ans1 = -1
            
            
for i in range(N):
    for j in range(M):
        if maxV < after_tomato[i][j] :
            maxV = after_tomato[i][j]
            ans2 = maxV - len(list1)
        else:
            ans2 = 0
            


if ans1 != -1:
    print(ans2)
else:
    print(ans1)
