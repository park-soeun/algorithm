import sys

def dfs(v, N):
    visited = [0] * (N + 1)
    visited[v] = 1
    stk = []
    stk.append(v)
    sol.append(v)
    while stk:
        for d in range(1, N + 1):
            if visited[d] == 0 and adj[v][d] == 1:
                visited[d] = 1
                sol.append(d)
                stk.append(v)
                v = d
                break
        else:
            v = stk.pop()
    return sol
    


V, E = map(int, sys.stdin.readline().rstrip().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
answer = []
visited2 = [0] * (V + 1)
cnt = 0
for _ in range(E):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adj[n1][n2] = adj[n2][n1] = 1
for i in range(1, V):
    if visited2[i] == 0:
        sol = []
        dfs(i, V)
        cnt += 1
        for j in range(len(sol)):
            visited2[sol[j]] = 1
for i in range(1, len(visited2)):
    if visited2[i] == 0:
        cnt += 1
print(cnt)