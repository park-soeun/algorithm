def solution(tickets):
    stk = []
    visited = [0] * len(tickets)
    stk.append(["ICN", "ICN"])
    sol = []
    answer = []
    sol.append("ICN")
    tickets = sorted(tickets, key = lambda x : x[1])
    s = "ICN"
    while stk:
        for d in range(len(tickets)):
            if visited[d] == 0 and s == tickets[d][0]:
                stk.append(tickets[d])
                sol.append(tickets[d][1])
                visited[d] = 1
                s = tickets[d][1]
                break
        else:
            s = stk.pop()[1]
    
    
    return sol
    