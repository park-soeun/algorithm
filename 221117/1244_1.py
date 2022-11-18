import sys
button = int(sys.stdin.readline().rstrip())
button_stat = [3] + list(map(int, sys.stdin.readline().rstrip().split()))
student = int(sys.stdin.readline().rstrip())
stu_stat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(student)] 
print()
for i in range(len(stu_stat)):
    # 남학생
    if stu_stat[i][0] == 1:
        for j in range(1, button + 1):
            if j % stu_stat[i][1] == 0:
                if button_stat[j] == 0:
                    button_stat[j] = 1
                else:
                    button_stat[j] = 0
    # 여학생
    else:
        k = 0
        print(k)
        print(button_stat[stu_stat[i][1] + k])
        print(button_stat[stu_stat[i][1] - k])
        print('이거 위에')
        while button_stat[stu_stat[i][1] + k] >= 0 and button_stat[stu_stat[i][1] - k] >= 0 and button_stat[stu_stat[i][1] + k] == button_stat[stu_stat[i][1] - k]:
            print('됐다')
            if button_stat[stu_stat[i][1] + k] == 0:
                print('여기')
                button_stat[stu_stat[i][1] + k] = 1
                button_stat[stu_stat[i][1] - k] = 1
                k += 1
            else:
                print('저기')
                button_stat[stu_stat[i][1] + k] = 0
                button_stat[stu_stat[i][1] - k] = 0
                k += 1
        
    print(*button_stat[1:])

