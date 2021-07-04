# Nqueen 처럼 생각해봐 너 굳이 좌표를 만들었니?? 아니잖아 그냥의 가상의 것이라고 생각해봐

def DFS(n,row,col):
    global result
    if n==2:
        if row==r and col==c:
            print(result)
            exit(0)
            return
        result+=1
        
        if row==r and col == c+1:
            print(result)
            exit(0)
            return
        result+=1
        
        if row+1==r and col == c:
            print(result)
            exit(0)
            return
        result+=1
        
        if row+1==r and col+1==c:
            print(result)
            exit(0)
            return
        result+=1
        return
        
    DFS(n/2,row,col)
    DFS(n/2,row,col+n/2)
    DFS(n/2,row+n/2,col)
    DFS(n/2,row+n/2,col+n/2)
    
result =0
N,r,c = map(int,input().split())
DFS(2**N,0,0)
        
        
        