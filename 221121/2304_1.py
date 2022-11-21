import sys
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 오른쪽에서 가장 큰 거 까지의 길이 곱하기 거리
# 피크 기준으로 왼쪽 오른쪽 하기? 좌우대칭으로 
arr.sort()
# print(arr)
width = arr[0][0]
height = arr[0][1]
first = arr.pop(0)
# print(first)
print(arr)
result = 0
for i in range(len(arr)):
    
    if arr[i][1] > height:
        result += (arr[i][0] - width) * height
        width = arr[i][0]
        height = arr[i][1]
    else:
        continue
print(result)