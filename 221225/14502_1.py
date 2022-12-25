import sys
from collections import deque

def bfs(si, sj):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        for di, dj  in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] != -1:
                if tomato[ni][nj] == 0:
                    queue.append((ni, nj))
                    tomato[ni][nj] = tomato[i][j] + 1
                elif tomato[ni][nj] > 1:
                    if tomato[ni][nj] > tomato[i][j] + 1:
                        tomato[ni][nj] = tomato[i][j] + 1
                        queue.append((ni, nj))
                    
    return visited


M, N = map(int, sys.stdin.readline().rstrip().split())
tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
start = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start.append([i, j])
for i in range(len(start)):
    bfs(start[i][0], start[i][1])
answer = 0
maxV = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            answer = -1
            break
        if maxV < tomato[i][j]:
            maxV = tomato[i][j]

if answer != -1:
    print(maxV - 1)
else:
    print(answer)
        
