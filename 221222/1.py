import sys

def dfs(si, sj, ei, ej, N):
    stk = []
    visited = [[0] * N for _ in range(N)]
    stk.append([si, sj])
    visited[si][sj] = 1
    while stk:
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != '1':
                if ni == ei and nj == ej:
                    return 1
                else:
                    stk.append([si, sj])
                    visited[ni][nj] = 1
                    si, sj = ni, nj
                    break
        else:
            si, sj = stk.pop()
    return 0





T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si = i
                sj = j
            elif arr[i][j] == '3':
                ei = i
                ej = j
    sol = dfs(si, sj, ei, ej, N)
    print(sol)


    