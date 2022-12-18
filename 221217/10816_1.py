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
            result[i] += 1
            j = 1
            while middle + j <= N - 1 :
                
                if num_cards[middle + j] == arr[i]:
                    result[i] += 1
                    j += 1
                else:
                    break
            k = 1
            while middle - k >= 0:
  
                if num_cards[middle - k] == arr[i]:
                    result[i] += 1
                    k += 1
                else:
                    break
            break
            
        elif num_cards[middle] < arr[i]:
            lower = middle + 1
        else:
            upper = middle - 1
            
    
print(*result)