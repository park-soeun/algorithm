import sys

n = int(sys.stdin.readline().rstrip())
arr = []
arr2 = []
tmp = []
ele = 1
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
print('-----')
for j in range(n):
    while ele < n :
        if arr[j] > ele:
            tmp.append(ele)
            ele += 1
            print('+')
            print(f'j는 {j} ele + {ele}')

        elif arr[j] == ele:
            tmp.append(ele)
            ele += 1
            print('+요기')
            arr2.append(tmp.pop())
            print('-요기')
            print(f'j는 {j} ele + {ele}')
            break
        else:
            arr2.append(tmp.pop())
            print('-')
            ele += 1
            print(f'j는 {j} ele + {ele}')

            break
    
