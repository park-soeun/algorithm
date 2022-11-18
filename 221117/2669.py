import sys
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(4)] 
result = 0
paper = [[0] * 100 for _ in range(100)]
for i in range(4):
    for p in range(arr[i][0], arr[i][2]):
        for q in range(arr[i][1], arr[i][3]):
            if paper[p][q] == 0:
                paper[p][q] = 1
                result += 1
        
print(result)