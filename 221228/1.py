def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = []
    stk = []
    adj = [[0] * 50 for _ in range(50)]
    visited = [[0] * 50 for _ in range(50)]
    
    stk.append((characterX, characterY))
    visited[characterX, characterY] = 1
    while stk:
        i, j = stk.pop(0)
        if i == itemX and j == itemY:
            answer.append(visited[i][j])
        for di, dj in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            ni = i + di
            nj = j + dj
            if 0 <= ni < 50 and 0 <= nj < 50 and visited[ni][nj] == 0 and adj[ni][nj] != 0:
                stk.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 17
