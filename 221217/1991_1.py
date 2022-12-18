import sys
while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if arr != [0]:
        k = arr.pop(0)
        
    else:
        break