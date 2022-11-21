import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
i = 0
tmp = sum(arr[:K])
result = [tmp]
for i in range(0, len(arr) - K):
    tmp = tmp - arr[i] + arr[i + K]
    result.append(tmp)
print(max(result))