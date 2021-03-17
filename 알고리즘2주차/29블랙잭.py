import sys
N,M = map(int,input().split())
numbers=list(map(int,sys.stdin.readline().split()))

score = 0
def DFS(L,res,idx):
    global score
    if L==3:
        if res<=M:
            score = max(score,res)
        return
    for i in range(idx,N):
        DFS(L+1,res+numbers[i],i+1)
DFS(0,0,0)
print(score)