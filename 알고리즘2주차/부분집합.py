

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

a = [1,2,3]
def permutation(L,res,me):
    if L == 2:
        print(res)
        return
    
    for i in range(3):
        if me!= i
            permutation(L+1,res+str(a[i]),me)

permutation(0,"")


