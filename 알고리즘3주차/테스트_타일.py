def fibo(n):
    dp_arr = [0,1,2]
    for i in range(3,n+1):
        num = (dp_arr[i-1]+dp_arr[i-2])%15746
        dp_arr.append(num)
    return dp_arr[n]
    
N = int(input())
print(fibo(N))

