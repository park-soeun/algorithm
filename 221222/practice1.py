def BFS(G, v, n):
    visited = [0] * (n + 1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        visit(t) 
        