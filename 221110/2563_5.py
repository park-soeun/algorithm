import sys
num = int(sys.stdin.readline().rstrip())
arr = []
paper = [[0 for _ in range(100)] for _ in range(100)] 
for _ in range(num):
    ele = list(map(int, sys.stdin.readline().rstrip().split()))
    ele2 = []
    ele2.append(ele[0])
    ele2.append(ele[1])
    arr.append(ele2)
for ele in range(len(arr)):
    for i in range(10):
        for j in range(10):
            paper[arr[ele][0] + i][arr[ele][1] + j] = 1
            paper[arr[ele][0] + j][arr[ele][1] + i] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)

