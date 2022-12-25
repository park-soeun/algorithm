import sys

def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]
    queue = []
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        if maze[i][j] == 3:
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = di + i
            nj = dj + j
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti = i
                stj = j
                break
        for j in range(N):
            if maze[i][j] == 3:
                ei = i
                ej = j
                break
    answer = bfs(sti, stj, N)
    print(f'#{tc + 1} {answer} ')
    