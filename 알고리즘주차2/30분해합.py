def split_num_sum(N):
    res = 0
    while N>0:
        res+=N%10
        N=N//10
    return res

N = int(input())
res = 0
limit = 1000000
for i in range(1,limit+1):
    if split_num_sum(i)+i==N:
        res = i
        break
print(res)
    