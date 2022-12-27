def solution(n, computers):
    answer = []
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        stk = []
        sol = []
        stk.append(i)
        sol.append(i)
        while stk:
            for d in range(n):
                if visited[d] == 0 and computers[i][d] == 1:    
                    stk.append(i)
                    sol.append(sol[-1] + 1)
                    visited[d] = visited[i] + 1
                    i = d
             
                
                    
            else:
                i = stk.pop()    
        
        answer.append(sol)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))