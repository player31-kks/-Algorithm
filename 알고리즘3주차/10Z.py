

N,r,c = map(int,input().split())
arr = [[0]*2**N for i in range(2**N)]
cnt = 0

def print2D(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            print(arr[row][col], end=" ")
        print()
    print()

def isZ(arr):
    return len(arr)==2 and len(arr[0])==2

def writeNum(arr):
    global cnt
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            arr[row][col] = cnt
            cnt+=1
            
            
def split_row_half(arr,direction):
    
    mid = len(arr[0])//2
    new_arr = []
    if direction=="L":
        for row in range(len(arr)):
            new_arr.append(arr[row][:mid])
    elif direction=="R":
        for row in range(len(arr)):
            new_arr.append(arr[row][mid:])
    return new_arr
    

def makeZ(arr):
    if isZ(arr):
        writeNum(arr)
        return arr

    mid = len(arr)//2
    
    a=makeZ(split_row_half(arr[:mid],"L"))
    b=makeZ(split_row_half(arr[:mid],"R"))
    
    half_one = []
    for row in range(len(a)):
        r=a[row]+b[row]
        half_one.append(r)
        
    c=makeZ(split_row_half(arr[mid:],"L"))
    d=makeZ(split_row_half(arr[mid:],"R"))
    
    half_two = []
    for row in range(len(c)):
        r = c[row]+d[row]
        half_two.append(r)
    
    return half_one+half_two

res=makeZ(arr)
print(res[r][c])