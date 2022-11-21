import sys
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort()
peak = 0
for i in range(len(arr)):
    if arr[i][1] >= peak:
        peak = arr[i][1]
        peak_point = i
        peak_width = arr[i][0]
width = arr[0][0]
height = arr[0][1]
first = arr.pop(0)
last = arr.pop()
result = 0

result += peak
for i in range(len(arr)):
    if i < peak_point:
        if arr[i][1] > height:
            result += (arr[i][0] - width) * height
            width = arr[i][0]
            height = arr[i][1]

width = peak_width
height = peak
print(result)
for i in range(-1, -(len(arr)), -1):
    # print(i)
    if arr[i][0] > peak_width:
        if arr[i][1] < height and arr[i][1] > last[1]:
            result += (arr[i][0] - width) * height
            
            
            
print(width, height)
result += (last[0] - width) * last[1]

print(result)
