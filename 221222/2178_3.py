import sys
def dfs(si, sj, ei, ej):
    sol = []
    stk = []
    visited = [[0] * M for _ in range(N)]
    stk.append([si, sj])
    sol.append([si, sj])
    visited[si][sj] = 1
    while stk:
        for di, dj in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            ni = si + di
            nj = sj + dj
            if 0 <= ni <= ei and 0 <= nj <= ej and visited[ni][nj] == 0 and arr[ni][nj] == '1':
                if ni == ei and nj == ej:
                    ans.append(visited[si][sj] + 1)
                    si, sj = stk.pop()
                    break
                    
                visited[ni][nj] = visited[si][sj] + 1
                stk.append([si, sj])
                
                si = ni
                sj = nj
                break
        else:
            si, sj = stk.pop()
    return visited        
    

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
ans = []
answer = dfs(0, 0, N - 1, M - 1)
print(min(ans))