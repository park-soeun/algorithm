def solution(tickets):
    stk = []
    visited = [0] * len(tickets)
    stk.append(["ICN", "ICN"])
    sol = []
    sol.append("ICN")
    while stk:
        depart = stk.pop()
        for i in range(len(tickets)):
            if depart[1] == tickets[i][0]:
                stk.append(tickets[i])
                sol.append(tickets[i][1])
                visited[i] = 1
            
            
            
            
        #     if depart == tickets[i][0] and visited[i] == 0:
        #         tickets[i].append(i)
        #         tmp.append(tickets[i])
        # sorted(tmp, key = tmp[1])
        # stk.append(tmp[0][1])
        # stk.append(tmp[0][0])
        # sol.append(tmp[0][1])
        
    return sol