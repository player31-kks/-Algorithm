def DFS(L,equ):
    if L==N+1:
        check=equ.replace(" ","")
        res = eval(check)
        if res==0:
            result.append(equ)
        return
    DFS(L+1,equ+f'+{L}')
    DFS(L+1,equ+f' {L}')
    DFS(L+1,equ+f'-{L}')

T = int(input())
for _ in range(T):
    N = int(input())
    result = []
    DFS(2,"1")
    result.sort()
    for r in result:
        print(r)
    print()
    