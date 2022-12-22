def dfs(s, N):
    visited = [0] * N
    sol = []
    stk = []
    sol.append(s)
    stk.append(s)
    while stk:
        for d in range(1, N):
            if visited[d] == 0 and adj[s][d] == 1:
                visited[d] = 1
                stk.append(s)
                sol.append(d)
                s = d
                break
        else:
            s = stk.pop()

    return sol

def bfs(s, N):
    visited = [0] * N
    q = []
    
    q.append(s)
    visited[s] = 1
    sol.append(s)

    while q:
        s = q.pop()
        for e in range(1, N):
            if visited[e] == 0 and adj[s][e] == 1:
                q.append(e)
                sol.append(e)
                visited[e] = 1
