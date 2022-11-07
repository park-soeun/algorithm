import sys
line = sys.stdin.readline().rstrip()
stick = []
result = 0
for i in range(len(line)):
    if line[i] == '(':
        stick = []
        laser = 0
        stick.append('(')
        for j in range(i + 1, len(line)):
            if len(stick) == 0:
                result += laser
            else:
                if line[j] == '(':
                    stick.append('(')
                elif line[i + 1] == ')':
                    laser += 1
                elif line[j] == ')':
                    stick.pop()
            
            
            
print(result)