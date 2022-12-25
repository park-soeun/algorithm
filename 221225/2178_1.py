import sys

def bfs(n, m):
    # visited 배열 만들기
    # 큐 만들기
    # 인큐 하기
    global visited
    visited = [[0] * (m) for _ in range(n)]
    queue = []
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        i, j = queue.pop(0)


        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return visited
    
    


N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
bfs(N, M)
print(visited[N - 1][M - 1])


