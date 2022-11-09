import sys
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]
num = list(map(int, sys.stdin.readline().rstrip().split())) 
num1 = list(map(int, sys.stdin.readline().rstrip().split())) 
num2 = list(map(int, sys.stdin.readline().rstrip().split())) 
num3 = list(map(int, sys.stdin.readline().rstrip().split())) 
num4 = list(map(int, sys.stdin.readline().rstrip().split())) 
num = num + num1 + num2 + num3 + num4

for no in range(len(num)):
    for i in range(5):
        for j in range(5):
            if num[no] == arr[i][j]:
                arr[i][j] = 'x'
            