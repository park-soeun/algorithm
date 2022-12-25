import sys

def dfs(s, N):
    visited = [0] * (N + 1)
    stk = []
    stk.append(s)
    visited[s] = 1
    while stk:
        for d in range(1, V + 1):
            if visited[d] == 0 and adj[s][d] == 1:
                visited[d] = 1
                sol.append(d)
                stk.append(s)
                s = d
                break
        else:
            s = stk.pop()
    return sol
        





V = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
adj = [[0] * (V + 1) for _ in range(V + 1)]
sol = []
for _ in range(E):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adj[n1][n2] = adj[n2][n1] = 1
    
dfs(1, V + 1)
print(len(sol))