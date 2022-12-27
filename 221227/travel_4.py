def solution(tickets):
    answer = []
    routes = dict()
    
    for start, end in tickets:
        if start not in tickets:
            routes[start] = [end]
        else:
            routes[start].append(end)
            
    for r in routes.keys():
        routes[r].sort(reverse = True)
        
    stk = ["ICN"]
    while stk:
        top = stk[-1]
        
        if top not in routes or len(routes[top]) == 0:
            answer.append(stk.pop())
        else:
            stk.append(routes[top].pop())
            
    return answer[::-1]
