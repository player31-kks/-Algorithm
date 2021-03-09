test_num = int(input())

for _ in range(test_num):
    H,W,N = map(int,input().split())
    y = N%H
    x = (N//H)+1
    
    if y==0:
        y = H
        x = (N//H)
    print(f"{y*100+x}")
    