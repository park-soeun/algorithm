import sys

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = map(int, sys.stdin.readline().rstrip().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    visited = [0] * (V + 1)
    stk = []
    sol = []
    s = 1
    stk.append(s)
    sol.append(s)
    while stk:
        for d in range(1, V + 1):
            if visited[d]:
                continue
            if adj[s][d] == 1:
                visited[d] = 1
                stk.append(d)
                sol.append(d)
                s = d

        else:
            s = stk.pop()
    print(*sol)