M,N = map(int,input().split())

check=[False]*(M+1)
def DFS(L,res):
    if L == N:
        print(res)
        return
    
    for i in range(1,M+1):
        if check[i]==False:
            check[i]=True    
            DFS(L+1,res+f'{i} ')
            check[i]=False
    
DFS(0,"")