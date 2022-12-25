I = [1, 2, 3, 4]
n = len(I)
r = 2
answer = []

def dfs(idx, list):
    if len(list) == r:
        answer.append(list[:])
    for i in range(idx, n):
        dfs(i + 1, list+[I[i]])
        print(list[:])
        
dfs(0, [])
print(answer)