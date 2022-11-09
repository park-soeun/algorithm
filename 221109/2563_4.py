import sys
num = int(sys.stdin.readline().rstrip())
arr = []
for i in range(num):
    ele = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(ele)
all = num * 100
width_arr = []
height_arr = []
for i in range(num):
    for j in range(i + 1, num):
        if abs(arr[i][0] - arr[j][0]) < 10:
            if abs(arr[i][1] - arr[j][1]) < 10:
                if arr[i][0] < arr[j][0]:
                    width = arr[i][0] + 10 
                    
                elif arr[i][0] > arr[j][0]:
                    width = arr[j][0] + 10 
                elif arr[i][0] == arr[j][0]:
                    width = 10
                if arr[i][1] < arr[j][1]:
                    height = arr[i][1] + 10 
                elif arr[i][1] > arr[j][1]:
                    height = arr[j][1] + 10 
                elif arr[i][1] == arr[j][1]:
                    height = 10
                width_arr.append(width)
                height_arr.append(height)
print(width_arr)
print(height_arr)
