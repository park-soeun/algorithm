import sys
num = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cntP_l = []
cntM_l = []

cntP = 1
for i in range(num - 1):
    if arr[i] <= arr[i + 1]:
        print(i, i+1)
        cntP += 1
    elif arr[i] > arr[i + 1]:
        print(f'plus {i}')
        print(cntP)
        cntP = 1
    cntP_l.append(cntP)
    
print()

cntM = 1
for i in range(num - 1):
    if arr[i]  >= arr[i + 1]:
        print(i)
        cntM += 1
        
    elif arr[i] < arr[i + 1]:
        cntM = 1
    cntM_l.append(cntM)
print(cntP_l, cntM_l)
if len(cntP_l) == 0 or len(cntM_l) ==0:
    print(max(cntP, cntM))
else:
    print(max(max(cntP_l), max(cntM_l)))
