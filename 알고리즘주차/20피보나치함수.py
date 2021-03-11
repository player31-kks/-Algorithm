N = int(input())

def DP(num):
    if num == 0:
        return (1,0)
    if num ==1:
        return (0,1)
    dp_arr = [(1,0),(0,1)]
    
    for i in range(2,num+1):
        first_zero_count,first_one_count=dp_arr[i-2]
        second_zero_count,second_one_count = dp_arr[i-1]
        new_zero_count = first_zero_count+second_zero_count
        new_one_count = first_one_count+second_one_count
        dp_arr.append((new_zero_count,new_one_count))
    return dp_arr[num]

for _ in range(N):
    zero,one = DP(int(input()))
    print(zero,one)
    