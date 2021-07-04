from collections import deque
ML,MR,TL,TR = input().split()

def game(a,b):
    judgment = deque(['S','P','R'])
    find = judgment.index(a)
    while True:
        if judgment[find]==b:
            break
        judgment.rotate(-1)
        cnt+=1
    return cnt
    
    

if ML==MR==TL==TR:
    print("?")
elif ML==MR and TL==TR:
    judg = game(ML,TL)
    if judg==0:
        pass
    elif judg==1:
        pass
    else:
        
elif ML==MR:
    game(ML,TL)
elif TL==TR:
    game(ML,TL)
else:
    print("?")