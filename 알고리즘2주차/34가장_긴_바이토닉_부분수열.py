N = int(input())
numbers = list(map(int,input().split()))
numbers.insert(0,0)

dp_arr_max = [0]*(N+1)
dp_arr_min = [0]*(N+1)
for i in range(1,N+1):
    max_num = 0
    for j in range(i-1,0,-1):
        if numbers[i] > numbers[j] and max_num < dp_arr_max[j]:
            max_num = dp_arr_max[j]
    dp_arr_max[i] = max_num+1

for i in range(N,0,-1):
    max_num = 0
    for j in range(i+1,N+1):
        if numbers[i] > numbers[j] and max_num < dp_arr_min[j]:
            max_num = dp_arr_min[j]
    dp_arr_min[i] = max_num+1

res = 0
for i in range(1,N+1):
    res=max(dp_arr_max[i]+dp_arr_min[i]-1,res)
print(res)