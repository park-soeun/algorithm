import sys

def dfs(v, N):
    visited = [0] * (V + 1)
    stk = []
    stk.append(v)
    visited[v] = 1
    sol.append(v)
    while stk:
        for d in range(1, V):
            if visited[d] == 0 and adj[v][d] == 1:
                visited[d] = 1
                sol.append(d)
                stk.append(v)
                v = d
                break
        else:
            v = stk.pop()
    return sol
                
    


T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    sol = []
    for i in range(E):
        n1, n2 = map(int, sys.stdin.readline().rstrip().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    dfs(1, V + 1)    
    print(*sol)
        
