def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = []
    stk = []
    visited = [[0] * 50 for _ in range(50)]
    visited2 = [[0] * 50 for _ in range(50)]
    adj = [[0] * 50 for _ in range(50)]
    for i in range(len(rectangle)):
        for w in range(rectangle[i][0], rectangle[i][2] + 1):
            for h in range(rectangle[i][1], rectangle[i][3] + 1):
                adj[w][h] += 1
    for i in range(len(rectangle)):
        for w in range(rectangle[i][0] + 1, rectangle[i][2]):
            for h in range(rectangle[i][1] + 1, rectangle[i][3]):
                adj[w][h] = 0
    
    stk.append((characterX, characterY))
    visited[characterX][characterY] = 1
    sol = []
    sol.append([characterX, characterY])
    i = characterX
    j = characterY
    
    
    while stk:
        for di, dj in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            ni = i + di
            nj = j + dj
            if ni == itemX and nj == itemY:
                # if answer:
                #     answer.append(len(sol) - answer[0] + 1)
                # else:
                answer.append(len(sol))
                
                i, j = stk.pop()
                break
            elif 0<= ni < 50 and 0 <= nj < 50 and visited[ni][nj] == 0 and adj[ni][nj] != 0:
               
                sol.append([ni, nj])
                stk.append((i, j))
                visited[ni][nj] = 1
                i, j = ni, nj
                break
        else:
            i, j = stk.pop()
            
    stk2 = []
    stk2.append((characterX, characterY))
    sol2 = []
    sol2.append([characterX, characterY])

    while stk2:
        for di, dj in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            ni = i + di
            nj = j + dj
            if ni == characterX and nj == characterY:
                total = len(sol2)
            elif 0<= ni < 50 and 0 <= nj < 50 and visited2[ni][nj] == 0 and adj[ni][nj] != 0:

                sol2.append([ni, nj])
                stk2.append((i, j))
                visited2[ni][nj] = 1
                i, j = ni, nj
                break
        else:
            i, j = stk2.pop()
            
    
    print(total)
    
    print(answer)
    answer.append(total - answer[0])
    
    print(answer)
    answer = sorted(answer)
    return min(answer)
 
  