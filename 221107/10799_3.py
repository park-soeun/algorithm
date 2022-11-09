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
            if line[j] == ')':
                stick.pop()
                

            
            
            
# print(result)