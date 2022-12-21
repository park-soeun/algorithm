import sys
V = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
adj = [[0] * (V + 1) for _ in range(V + 1)]
stk = []
sol = []
visited = [0] * (V + 1)
for i in range(E):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1
s = 1
stk.append(s)
sol.append(s)
while stk:
    for d in range(1, V + 1):
        
        if adj[s][d] == 1 and visited[d] == 0:
            visited[d] = 1
            stk.append(s)
            sol.append(d)
            s = d
            break
    else:
        s = stk.pop()
cnt = 0
for i in range(V + 1):
    if visited[i] == 1 and i != 1:
        cnt += 1

print(cnt)