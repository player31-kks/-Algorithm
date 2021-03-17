T = int(input())

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    

for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = distance(x1,y1,x2,y2)
    r1,r2 = max(r1,r2),min(r1,r2)

    if d==0 and r1==r2: #같은 원일 때 
        print(-1)
    elif r1+r2==d or r1-r2==d: #내접 or 외접
        print(1)
    elif r1-r2 < d <r1+r2: # 겹치는 부분
        print(2)
    else: # 그외
        print(0)