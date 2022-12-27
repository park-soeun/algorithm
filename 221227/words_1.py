def solution(begin, target, words):
    
    stk = []
    sol = []
    sol.append(begin)
    stk.append(begin)
    visited = [0] * len(words)
    
    while stk:
        top = stk.pop()
        if top == target:
            return sol
        for i in range(len(words)):
            tmp = words[i]
            for j in range(len(begin)):
                if top[j + 1:] == target[j + 1:] and top[:j] == target[:j] and target in words:
                    return sol
                elif top[j + 1:] == tmp[j + 1:] and top[:j] == tmp[:j] and visited[i] == 0:
                    stk.append(tmp)
                    sol.append(tmp)
                    visited[i] = 1
                    break
               
          
    return sol
            
    
    
