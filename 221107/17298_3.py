# 큰 수를 무조건 다 pop해서 넣어보고 젤 꼭데기꺼 뱉어내게
import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(T)]
stk = []
for i in range(T):
    while(stk and arr[stk[-1]] < arr[i]):
        result[stk[-1]] = arr[i]
        stk.pop()
    stk.append(i)
    