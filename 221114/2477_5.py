import sys
melon = int(sys.stdin.readline().rstrip())
x_list = []
y_list = []
for i in range(6):
    direc, how = map(int, sys.stdin.readline().rstrip().split())
    if direc == 1:
        x_list.append(how)
    elif direc == 2:
        x_list.append(how)
    elif direc == 3:
        y_list.append(how)
    else:
        y_list.append(how)