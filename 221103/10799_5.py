import sys
line = sys.stdin.readline().rstrip()
for i in range(len(line)):
    if line[i] == '(':
        stick = []
        laser = 0
        stick.append(line[i])
        for j in range(i, len(line)):
            if line[j] == '(':
                if line[j + 1] == ')':
                    laser += 1
                else:
                    stick.append(line[j])
            else:
                stick.append(line[j])
        print(stick)
                