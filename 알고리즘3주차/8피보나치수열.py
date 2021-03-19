memo ={}

def fibo(n):
    if n in memo:
        return memo[n]
    if n<2:
        return n
    memo[n] = fibo(n-1)+fibo(n-2)
    return memo[n]

N = int(input())
print(fibo(N))