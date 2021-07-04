import sys
sys.setrecursionlimit(3000)

T = int(input())

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def print2D(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    print()

def DFS(row,col):
    global cnt
    if MAP[row][col]==0:
        return
    MAP[row][col]= 0
    for i in range(4):
        new_row = row+dr[i]
        new_col = col+dc[i]
        if 0<=new_row<N and 0<=new_col<M and MAP[new_row][new_col]==1:
            DFS(new_row,new_col)
        

for _ in range(T):
    M,N,K = map(int,input().split())
    MAP =[[0]*M for i in range(N)]
    
    for _ in range(K):
        r,c = map(int,input().split())
        MAP[c][r] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j]==1:
                cnt+=1
                DFS(i,j)
    print(cnt)
        
    
        