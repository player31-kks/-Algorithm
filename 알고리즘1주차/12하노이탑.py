
num = int(input())
def hanoi(n,start,between,end):
    if n==1:
        print(start,end)
        return
    hanoi(n-1,start,end,between)
    print(start,end)
    hanoi(n-1,between,start,end)
    
print(pow(2,num) - 1)
hanoi(num,1,2,3)

