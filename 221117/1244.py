import sys
button = int(sys.stdin.readline().rstrip())
button_stat = [3] + list(map(int, sys.stdin.readline().rstrip().split()))
student = int(sys.stdin.readline().rstrip())
stu_stat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(student)] 
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
        while len(button_stat) > stu_stat[i][1] + k > 0 and len(button_stat) > stu_stat[i][1] - k > 0 and button_stat[stu_stat[i][1] + k] == button_stat[stu_stat[i][1] - k]:
            if button_stat[stu_stat[i][1] + k] == 0:
                button_stat[stu_stat[i][1] + k] = 1
                button_stat[stu_stat[i][1] - k] = 1
                k += 1
            else:
                button_stat[stu_stat[i][1] + k] = 0
                button_stat[stu_stat[i][1] - k] = 0
                k += 1
        
for i in range(1, len(button_stat)):
    print(button_stat[i], end=" ")
    if i % 20 == 0:
        print()
    


