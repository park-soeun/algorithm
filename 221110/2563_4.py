import sys
num = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(num):
    ele = list(map(int, sys.stdin.readline().rstrip().split()))
    ele2 = []
    ele2.append(ele[0])
    ele2.append(ele[1])
    arr.append(ele2)
area = num * 100
result = 0
width_list = []
height_list = []
for i in range(num):
    for j in range(i + 1, num):
        width = 0
        height = 0
        if abs(arr[i][0] - arr[j][0]) < 10 and abs(arr[i][1] - arr[j][1]) < 10:
            if arr[i][0] < arr[j][0]:
                width_list.append(arr[i][0] + 10)
                width_list.append(arr[j][0])
                width = arr[i][0] + 10 - arr[j][0]
            else:
                width_list.append(arr[j][0] + 10)
                width_list.append(arr[i][0])
                width = arr[j][0] + 10 - arr[i][0]
                
            if arr[i][1] < arr[j][1]:
                height_list.append(arr[i][1] + 10)
                height_list.append(arr[j][1])
                height = arr[i][1] + 10 - arr[j][1]
                
            else:
                height_list.append(arr[j][1] + 10)
                height_list.append(arr[i][1])
                height = arr[j][1] + 10 - arr[i][1]
            
            area -= width * height
            print(area)
            
print(width_list)
print(height_list)
print(area)
            

       




        # for p in range(2):
        #     pass
        # for q in range(2):
        #     pass