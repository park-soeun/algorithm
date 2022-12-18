import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
# H를 거꾸로 부터 전부다 할 수 있지만 이진 탐색으로 해보겠다. 
lower = 0
upper = max(tree)
answer = 0

while lower <= upper:
    middle = (lower + upper) // 2
    bring_tree = 0
    for i in range(N):
        if tree[i] - middle > 0:
            bring_tree += tree[i] - middle    
        else:
            continue
    if bring_tree == M:
        answer = middle
        break
    elif bring_tree > M:
        answer = middle
        lower = middle + 1
    else:
        upper = middle - 1
print(answer)