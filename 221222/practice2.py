import sys

def dfs(s, N):
    visited = [0] * N
    stk = []
    sol = []
    stk.append(s)
    visited[s] = 1
    sol.append(s)
    while stk:
        for d in range(1, N):
            if visited[d] == 0 and adj[s][d]:
                stk.append(s)
                visited[d] = 1
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
            if visited[e] == 0 and adj[s][e] == 1:
                q.append(e)
                sol.append(e)
                visited[e] = 1

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    V, E = map(int, sys.stdin.readline().rstrip().split())

    adj = [[0] * (V + 1) for _ in range(V + 1)]
    sol = []
    for _ in range(E):
        n1, n2 = map(int, sys.stdin.readline().rstrip().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    bfs(1, V + 1)