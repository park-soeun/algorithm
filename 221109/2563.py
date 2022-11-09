import sys
num = int(sys.stdin.readline().rstrip())
arr = []
for i in range(num):
    ele = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(ele)
all = num * 100
for i in range(num):
    for j in range(i + 1, num):
        if abs(arr[i][0] - arr[j][0]) < 10:
            if abs(arr[i][1] - arr[j][1]) < 10:
                subst = abs((arr[i][0] - arr[j][0])) * abs(arr[i][1] - arr[j][1])
                print(subst)
                all -= subst                
print(all)
