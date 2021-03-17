N = int(input())
Numbers = list(map(int,input().split()))
Numbers.insert(0,0)
dp_arr = [0 for i in range(len(Numbers)+1)]

for idx in range(1,len(Numbers)):
    max_num =0
    for jdx in range(idx,0,-1):
        if Numbers[idx] > Numbers[jdx] and max_num <dp_arr[jdx]:
            max_num = dp_arr[jdx]
    dp_arr[idx] = max_num+1
    
print(max(dp_arr))