import sys

while True:
    line = sys.stdin.readline().rstrip()
    for i in range(len(line)):
        stk = []        
        if line[i] == '(':
            stk.append('(')
        elif line[i] == ')':
            if len(stk) != 0:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(')')
            else:
                    stk.append(')')
        elif line[i] == '[':
            stk.append('[')
        elif line[i] == ']':
            if len(stk) != 0:
                if stk[-1] == '[':
                    stk.pop()
                else:
                    stk.append(']')
            else:
                    stk.append(']')
        elif line[i] == '.':
            if len(stk) == 0:
                print('yes')
                break
            else:
                print('no')
                break

