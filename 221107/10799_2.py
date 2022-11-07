import sys
line = sys.stdin.readline().rstrip()
stk = []
for i in range(len(line)):
    if line[i] == '(':
        if line[i + 1] == ')':
            stk.append('x')
        else:
            stk.append('(')
    else:
        if line[i - 1] == '(':
            pass
        else:
            stk.append(')')
result = 0
for i in range(len(stk)):
    if stk[i] == '(':
        stick = []
        laser = 0
        stick.append('(')
        for j in range(i + 1, len(stk)):
            if len(stick) != 0:
                if stk[j] == '(':
                    stick.append('(')
                elif stk[j] == 'x':
                    laser += 1
                else: 
                    stick.pop()
        result += laser + 1
print(result)