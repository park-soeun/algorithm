import sys
line = sys.stdin.readline().rstrip()
stick = []
result = []
laser = 0
for i in range(len(line)):
    if line[i] == '(':
        if line[i + 1] == ')':
            if len(stick) == 0:
                break
            else:
                stick.append('(')
                laser += 1
        else:
            stick.append('(')
    elif line[i] == ')':
        