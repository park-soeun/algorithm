import sys

line = ''
while True:
    stk = []        
    line = list(input())
    if line == '.':
        break
    for i in range(len(line)):
        if line[i] == '(':
            stk.append('(')
        elif line[i] == ')':
            if len(stk) != 0:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(')')
            else:
                print('no')
                break
        elif line[i] == '[':
            stk.append('[')
        elif line[i] == ']':
            if stk[-1] == '[':
                stk.pop()
            else:
                stk.append(']')
            if len(stk) == 0:
                print('yes')
                break   
            else:
                print('no')
                break
       


