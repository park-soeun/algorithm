import sys
N = int(sys.stdin.readline().rstrip())
num_cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = [0] * M

num_cards.sort()

for i in range(M):
    lower = 0
    upper = N - 1
    
    while lower <= upper:
        middle = (lower + upper) // 2
        if num_cards[middle] == arr[i]:
            lower1 = (lower + middle) // 2
            upper1 = middle
            lower2 = middle
            upper2 = (upper - middle) // 2
            while lower1 <= upper1:
                middle1 = (lower1 + upper1) // 2
                if num_cards[middle1] == arr[i]:
                    
            
             
            
        elif num_cards[middle] < arr[i]:
            lower = middle + 1
        else:
            upper = middle - 1
            
    
print(*result)