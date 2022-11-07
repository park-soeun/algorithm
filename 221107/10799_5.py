import sys
line = sys.stdin.readline().rstrip()
result = 0
for i in range(len(line)):
    if line[i] == '(':
        stk = []
        cnt = 0
        stk.append('(')
        laser = 0
        for j in range(i + 1, len(line)):
            if len(stk) != 0:
                if line[j] == '(':
                    
                    stk.append('(')
                else:
                    if line[j - 1] == '(':
                        laser += 1
                        stk.pop()
                        cnt += 1
                    else:
                        
                        stk.pop()
                        cnt += 1
        
        if cnt == 1:
            pass
        else:
            result += laser + 1

                    
            
            # print(f'{i} 그리고 {laser} 그리고 {cnt}')

                
                
                    
        
    

    
print(result)