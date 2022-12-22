def dfs(s, N):
    visited = [0] * N
    sol = []
    stk = []
    sol.append(s)
    stk.append(s)
    while stk:
        for d in range(1, N):
            if visited[d] == 0 and adj[s][d]:
                visited[d] = 1
                stk.append(s)
                sol.append(d)
                s = d
                break
        else:
            s = stk.pop()


def bfs(s, N):
    q = []
    visited = [0] * N

    q.append(s)
    visited[s] = 1
    sol.append(s)

    while q:
        s = q.pop(0)
        for e in range(1, N):
            if visited[e] == 0 and adj[s][e] != 0:
                q.append(s)
                visited[e] = 1
                sol.append(e)



