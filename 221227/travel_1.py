def solution(tickets):
    stk = []
    visited = [0] * len(tickets)
    stk.append(["ICN", "ICN"])
    sol = []
    sol.append("ICN")
    while stk:
        depart = stk.pop()
        tmp = []
        for i in range(len(tickets)):
            if depart[1] == tickets[i][0] and visited[i] == 0:
                tickets[i].append(i)
                tmp.append(tickets[i])
                tmp.append([0,'ZZZZ',0])
            for p in range(len(tmp)):
                if tmp[p][1] > tmp[p + 1][1]:
                    tmp[p], tmp[p + 1] = tmp[p + 1], tmp[p]
            tmpp = [tmp[0][0], tmp[0][1]]
            stk.append(tmpp)
            sol.append(tmpp[1])
            visited[tmp[0][2]] = 1
            
            
            
            
        #     if depart == tickets[i][0] and visited[i] == 0:
        #         tickets[i].append(i)
        #         tmp.append(tickets[i])
        # sorted(tmp, key = tmp[1])
        # stk.append(tmp[0][1])
        # stk.append(tmp[0][0])
        # sol.append(tmp[0][1])
        
    return sol