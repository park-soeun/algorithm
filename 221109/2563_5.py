import sys
num = int(sys.stdin.readline().rstrip())
arr = []
for i in range(num):
    ele = list(map(int, sys.stdin.readline().split()))
    arr.append(ele)
x_arr = []
y_arr = []
for i in range(num):
    for j in range(i + 1, num):
        

print(arr)