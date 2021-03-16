
result = set()
N = int(input())
numbers = list(map(int,input().split()))

def DFS(L,res):
    if L == N:
        result.add(res)
        return
    DFS(L+1,res+numbers[L])
    DFS(L+1,res)
    
DFS(0,0)
result = list(result)
result.sort()

check = 0
print(result)
for num in result:
    if check!=num:
        print(check)
        break
    check+=1
    
    