def dfs(si, sj, ei, ej, N):
    stk = []
    visited = [[0] * N for _ in range(N)]
    stk.append([si, sj])
    visited[si][sj] = 1
    while stk:
        for di, dj in ([-1, 0], [0, 1], [1, 0], [0, -1]):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != '1':
                if ni == ei and nj == ej:
                    return 1

                else:
                    visited[ni][nj] = 1
                    stk.append([ni, nj])
                    si = ni
                    sj = nj
                    break
        else:
            si, sj = stk.pop()
    return 0

    

