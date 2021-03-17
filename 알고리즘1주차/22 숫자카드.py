def binarySearch(arr,target_num):
    left = 0
    right = len(arr)-1
    
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target_num:
            return 1
        elif arr[mid] > target_num:
            right = mid-1
        else:
            left = mid+1
    return 0


N = int(input())
Numbers = list(map(int,input().split()))
Numbers.sort()
M = int(input())
target_Numbers = list(map(int,input().split()))

res =[]
for target in target_Numbers:
    result=binarySearch(Numbers,target)
    res.append(result)

for r in res:
    print(r,end=" ")

