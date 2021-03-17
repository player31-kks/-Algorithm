def is_prime(n):
    if n<2:
        return False
    if n in (2,3):
        return True
    if n%2==0 or n%3==0:
        return False
    if n< 10:
        return True
    limit,k = n**0/5,5
    while(k<=limit):
        if n%k==0 or n%(k+2):
            return False
        k+=6
    return True

def prime(n):
    seive = [False,False]+[True]*(n-1)
    for k in range(2,int(n**0.5)+1):
        if seive[k]:
            seive[k*2::k] = [False]*((n-k)//k)
    return [x for x in range(n+1) if seive[x]]



M,N = map(int,input().split())
for i in range(M,N+1):
    if is_prime(i):
        print(i)


