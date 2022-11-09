import sys
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]
num = list(map(int, sys.stdin.readline().rstrip().split())) 
num1 = list(map(int, sys.stdin.readline().rstrip().split())) 
num2 = list(map(int, sys.stdin.readline().rstrip().split())) 
num3 = list(map(int, sys.stdin.readline().rstrip().split())) 
num4 = list(map(int, sys.stdin.readline().rstrip().split())) 
num = num + num1 + num2 + num3 + num4
cnt = 0
check3 = 0
check4 = 0
already_1 = []
already_2 = []
for no in range(len(num)):
    for i in range(5):
        for j in range(5):
            if num[no] == arr[i][j]:
                arr[i][j] = 'x'
                for i in range(5):
                    if i not in already_1:
                        x_cnt = 0
                        for j in range(5):
                            if arr[i][j] == 'x':
                                x_cnt += 1
                        if x_cnt == 5:
                            cnt += 1
                            already_1.append(i)
                for i in range(5):
                    if i not in already_2:
                        x_cnt = 0
                        for j in range(5):
                            if arr[j][i] == 'x':
                                x_cnt += 1
                        if x_cnt == 5:
                            cnt += 1
                            already_2.append(i)
                if check3 < 1:
                    for i in range(5):
                        x_cnt = 0
                        if arr[i][i] == 'x':
                            x_cnt += 1
                    if x_cnt == 5:
                        check3 += 1
                        cnt += 1
                if check4 < 1:
                    x_cnt = 0
                    for i in range(4,-1,-1):
                        if arr[4 - i][i] == 'x':
                            x_cnt += 1
                    if x_cnt == 5:
                        check4 += 1
                        cnt += 1
    if cnt == 3:
        print(no + 1)
        break