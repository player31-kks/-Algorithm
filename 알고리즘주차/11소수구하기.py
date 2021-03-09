def is_prime(n):
    if n<2:
        return False
    if n in (2,3):
        return True
    if n%2==0 or n%3==0:
        return False
    if n < 10:
        return True
    k,limit = 5,n**0.5
    while(k<=limit):
        if n%k==0 or n%(k+2)==0:
            return False
        k+=6
    return True

M,N = map(int,input().split())
for i in range(M,N+1):
    if is_prime(i):
        print(i)
