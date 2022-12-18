import sys
N = int(sys.stdin.readline().rstrip())
num_cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = [0] * M

def mergeSort(arr):
    
    if len(arr) > 1:
        # 쪼개는 과정
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        #합치는 과정 - 임시로 정렬
        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        #각각 남아있는 원소 합치기
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
            
    return arr
        
mergeSort(num_cards)


for i in range(M):
    lower = 0
    upper = N - 1
    
    # 첫번째 10 값을 찾아야 하고
    # 마지막 10 값을 찾아야 함
    while lower <= upper:
        middle = (lower + upper) // 2
        idx_lower = 0
        idx_upper = 0
        if num_cards[middle] == arr[i]:
            while True:
                j = 0
                k = 0
                if middle - j > 0:
                    if num_cards[middle - j] != arr[i]:
                        idx_lower = middle - j
                        break
                    elif num_cards[middle - j] == arr[i]:
                        j += 1
                    else:
                        idx_lower = -1
                        break
                
                if middle + k < N - 1:
                    if num_cards[middle + k] != arr[i]:
                        idx_upper = middle + k
                        break
                    elif num_cards[middle + k] == arr[i]:
                        k += 1
                    else:
                        idx_upper = N
                        break
                break
                    
                    
                
                    
                
                
                
                        
        elif num_cards[middle] < arr[i]:
            lower = middle + 1
        else:
            upper = middle - 1
            
        
        
        
        

    if idx_lower != 0 or idx_upper != 0:
        result[i] += idx_upper - idx_lower - 1
    
        
            
            
            
        
            
            
    
print(*result)