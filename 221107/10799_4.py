import sys
line = sys.stdin.readline().rstrip()
result = 0
for i in range(len(line)):
    if line[i] == '(':
        stk = []
        cnt = 0
        stk.append('(')
        laser = 0
        print(f'i는 {i}')
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
            else:
                # 한번 일 땐 빼
                if cnt == 1:
                    print(f'에러 {i}')
                    break
                    
                else:
                    print(i, laser)
                    result += laser + 1
                    break
                
                
                    
        
    

    
print(result)