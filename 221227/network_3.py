def solution(n, computers):
    result = []
    cnt = 0
    cnt_single = 0
    for i in range(n):
        visited2 = [0] * n
        visited = [0] * n
        stk = []
        sol = []
        stk.append(i)
        sol.append(i)
        visited[i] = 1
        while stk:
            for d in range(n):
                if visited[d] == 0 and computers[i][d] == 1:
                    visited[d] = 1
                    stk.append(i)
                    sol.append(d)
                    i = d
                elif visited[d] == 0 and computers[i][d] == 0:
                    cnt_single += 1
            else:
                i = stk.pop()
        result.append(sol)
        real = []
        
                    
        for j in range(len(result)):
            if sorted(result[j]) not in real:
                real.append(result[j])
        real_real = []
        for j in range(len(real)):
            for k in range(len(real[j])):
                if visited2[real[j][k]] == 0:
                    visited2[real[j][k]] = 1
                    if j not in real_real:
                        real_real.append(j)
                # else:
                #     real.pop(j)
                #     break
    return len(real_real)
                
#     print(real)
#     return len(real)

        
        
          
                      
                      
                  
        # cnt += 1
#         for j in range(len(result)):
#             for k in range(len(result[j])):
#                 if visited2[[result[j][k]]] == 0:
#                     visited2[[result[j][k]]] = cnt
            
# #             if visited2[r] == 0:
# #                 visited2[sol[j]] = cnt
        
        
    
    
    
    
    
    
    
