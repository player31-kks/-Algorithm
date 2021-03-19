def DFS(L,res,ex):
    if L==M:
        print(res)
        return
    for i in range(ex+1,N+1):
        DFS(L+1,res+str(i)+" ",i)

def permutation(L,res,me):
    if L ==2:
        print(res)
        return
    for i in range(1,N+1):
        if i == me:
            continue
        else:
            permutation(L+1,res+str(i),i)
        

N,M = map(int,input().split())
permutation(0,"",0)

