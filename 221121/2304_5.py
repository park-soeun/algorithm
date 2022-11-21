import sys
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# max peak 로 부터 양쪽으로 좁혀져 오는 느낌으로 하면 될 듯
arr.sort()

result = 0
peak_height = 0
for i in range(len(arr)):
    if arr[i][1] > peak_height:
        peak_height = arr[i][1]
        peak_point = i
        peak_width = arr[i][0]
result += peak_height
width = arr[0][0]
height = arr[0][1]
for i in range(1, peak_point):
    if height < arr[i][1]:
        result += (arr[i][0] - width) * height
        width = arr[i][0]
        height = arr[i][1]
result += (peak_width - width) * height
width = arr[-1][0]
height = arr[-1][1]

for i in range(-2, -(len(arr) - peak_point), -1):
    if arr[i][1] > height:
        result += (width - arr[i][0]) * height
        width = arr[i][0]
        height = arr[i][1]
result += (width - peak_width) * height
        

print(result)