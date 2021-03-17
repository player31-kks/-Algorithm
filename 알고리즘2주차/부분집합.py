

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

a = [1,2,3,4]
def permutation(L,res):
    if L == 2:
        print(res)
        return
    
    for i in range(4):
        permutation(L+1,res+[a[i]])


def DFS(L,res):
    #종료조건
    if L ==len(a):
        print(res)
        return
    else:
        DFS(L+1,res+str(a[L]))
        DFS(L+1,res)
permutation(0,[])