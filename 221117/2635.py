import sys
num = int(sys.stdin.readline().rstrip())
tmp = 0 
tmp = []
result_len = 0
result_arr = []

for i in range(num, -1, -1):
    arr = [num]
    arr.append(i)
    while arr[-2] - arr[-1] >= 0:
        arr.append(arr[-2] - arr[-1])
    tmp.append([len(arr), arr]) 
for i in range(len(tmp)):
    if tmp[i][0] > result_len:
        result_len = tmp[i][0]
        result_arr = tmp[i][1]

print(result_len)
print(*result_arr)
    