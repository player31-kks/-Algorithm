def find_minum_count(n,times):
    r = 0
    for time in times:
        r += 1/time
    return int(n/r)

def solution(n, times):
    
    go = find_minum_count(n,times)
    print(go)
    while True:
        result =0
        for time in times:
            if go < time:
                break
            result+=go//time
        if result >= n:
            print(go)
            break
        go+=1
        
    return go

n = 50000
times =[5,7,10,100,20,300]
solution(n, times)