import sys
num = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(num):
    ele = list(map(int, sys.stdin.readline().rstrip().split()))
    ele2 = []
    ele2.append(ele[0])
    ele2.append(ele[0] + 10)
    ele2.append(ele[1])
    ele2.append(ele[1] + 10)
    arr.append(ele2)
# print(arr)
for i in range(num):
    for j in range(i + 1, num):
        if arr[i][0] < arr[j][0]:
            # 이렇게 해도 되고 3보타 20큰애 라고 해도 될듯
            if arr[i][1] > arr[j][0]:
                width = arr[i][1] - arr[j][0]
            else:
                break
        if arr[i]
            
        else:
            if arr[j][1] > arr[i][0]:




        # for p in range(2):
        #     pass
        # for q in range(2):
        #     pass