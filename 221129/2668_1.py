import sys
N = int(sys.stdin.readline().rstrip())
arr1 = [0]
arr2 = [0]
arr3 = []
ans = 0
for i in range(1, N + 1):
    num = int(sys.stdin.readline().rstrip())
    arr1.append(i)
    arr2.append(num)
    arr3.append([num, i])

chain = []
# for i in range(N + 1):
#     for j in range(i, N + 1):
#         if 
var1 = 0
chain_num = 0
chain_list = []
while var1 < N + 1:
    
    chain = []
    chain.append(var1)
    chain.append(arr2[var1])
    var2 = 0
    chain_num = 1
    
    if arr1[var1] != arr2[var1]:
        cnt = 0
        while chain[0] != chain[-1] and cnt < N + 1:
            chain.append(chain[-1])
            chain.append(arr2[chain[-1]])
            chain_num += 1
            cnt += 1
            
            
        else:
            if len(chain) < N * N:
                chain_list.append(chain)
                var1 += 1
            
    else:
        
        chain.append(var1)
        var1 += 1
    # print(chain_num)
print(chain)
print(chain_list)

