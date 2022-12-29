def solution(n, L):
    answer = []
    for i in range(n):
        visited = [0] * n
        s = i
        visited[s] = 1
        stk = []
        sol = []
        stk.append(s)
        sol.append(s)
        while stk:
            for j in range(n):
                d = j
                if L[s][d] != 0 and visited[d] == 0:
                    stk.append(s)
                    sol.append(d)
                    visited[d] = 1
                    s = d
                    break
            else:
                s = stk.pop()
    sol.append(i)
    answer.append(sol)

    real = []
    for i in range(len(answer)):
        total = 0
        for j in range(n):
            total += L[answer[i][j]][answer[i][j + 1]]
        total += L[answer[i][-1]][answer[i][0]]
        real.append(total)
    
    return min(real)