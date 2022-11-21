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
last = arr.pop()

# print(arr)
result = 0
peak = 0
next_width = 0
next_height = 0
for i in range(len(arr)):
    if arr[i][1] > peak:
        peak = arr[i][1]
        peak_point = i
        peak_width = arr[i][0]
result += peak
print(width, height)
for i in range(len(arr)):
    if i < peak_point:
        if arr[i][1] > height:
            result += (arr[i][0] - width) * height
            print()
            print(arr[i][0], width, height)
            width = arr[i][0]
            height = arr[i][1]
            print(result)
            
        else:
            print('잉')
            print(arr[i][0], width, height)
result += (peak_width - width) * height
        
# print(last)
print(result)
print(last[0], peak_width, last[1])
result += (last[0] - peak_width) * last[1]
    # elif i > peak_point:
    #     if arr[i][1] < last[1]:
    #         result += (arr[i][0] - peak_width + 1) * last[1]
    #     else:
    #         # print(i)
    #         # print("이게 왜?")
    #         result += (arr[i][0] - peak_width + 1) * arr[i][1]

print(result)
