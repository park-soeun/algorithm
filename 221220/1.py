class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in range(len(S)):
        if S[i] not in prec and S[i] != ')':
            answer += S[i]
        else:
            if opStack.isEmpty():
                opStack.push(S[i])
            else:
                if S[i] == ')':
                    while opStack.peek() != '(':
                        answer += opStack.pop()
                    
                
                elif prec[opStack.peek()] >= prec[S[i]]:
                    
                    opStack.push(S[i])

                
                else:
                    opStack.push(S[i])
    
    
    while not opStack.isEmpty():
        answer += opStack.pop()  
    print(answer)
    return answer

solution("(A+B)*(C+D)")
print('ab+cd+*')
solution("A*B+C")
print('ab*c+')
solution("(A+B)*C")
print('ab+c*')