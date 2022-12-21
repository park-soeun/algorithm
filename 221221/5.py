def DFS(s, N):
    visited = [0] * N
    stk = []
    stk.append(s)
    visited[s] = 1
    sol.append(s)
    while stk:
        for d in range(1, N):
            if visited[d] == 0 and adj[s][d]:  # 안 가본, 연결된 노드면
                stk.append(s) # 나중에 돌아와서 나머지를 더 가보기 위해서 push
                visited[d] = 1
                sol.append(d)
                s = d
                break
        else:
            s = stk.pop()
 
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    sol = []
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = 1
    DFS(1, V + 1)
    print(f'#{test_case}', *sol)