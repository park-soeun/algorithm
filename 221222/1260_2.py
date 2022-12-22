def dfs(s, N):
    stk = []
    sol = []
    visited = [0] * (N)
    visited[s] = 1
    stk.append(s)
    sol.append(s)
    while stk:
        for d in range(1, N):
            if visited[d] == 0 and adj[s][d]:
                visited[d] = 1
                sol.append(d)
                stk.append(s)
                s = d
                break
        else:
            s = stk.pop()
    return sol
    
def bfs(s, N):
    q = []
    visited = [0] * N
    
    q.append(s)
    visited[s] = 1
    sol = []
    sol.append(s)
    while q:
        s = q.pop(0)
        for e in range(1, N):
            if visited[e] == 0 and adj[s][e]:
                visited[e] = 1
                q.append(e)
                sol.append(e)
    return sol

import sys
V, E, s = map(int, sys.stdin.readline().rstrip().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
sol = []
for _ in range(E):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1
sol1 = dfs(s, V + 1)
sol2 = bfs(s, V + 1)

print(sol1, sol2)
