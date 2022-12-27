def solution(tickets):
    answer = []
    routes = dict()
    
    for (start, end) in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    for r in routes.keys():
        routes[r].sort(reverse = True)
        
    stk = ["ICN"]
    while stk:
        top = stk[-1]
        
        if (top not in routes) or (not routes[top]):
            answer.append(stk.pop())
        else:
            stk.append(routes[top].pop())
    return answer[::-1]