a = [1,2,3]

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

def DFS(L,res):
    #종료조건
    if L ==len(a):
        print(res)
        return
    else:
        DFS(L+1,res+str(a[L]))
        DFS(L+1,res)
DFS(0,"hello")