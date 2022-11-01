import sys

A = list(sys.stdin.readline())
B = list(sys.stdin.readline())

for i in range(len(A)):
    if A == B:
        result = len(A)
    elif 