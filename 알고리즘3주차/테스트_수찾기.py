import sys

# in 연산자는 이분탐색보다 느리다는 것을 알게됨
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
M = int(input())
que = list(map(int,sys.stdin.readline().split()))

def binarySearch(arr,target):
    left = 0
    right = len(arr)-1
    
    while left<=right:
        mid = (left+right)//2
        
        if arr[mid]==target:
            return True
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid +1
    return False


for num in que:
    if binarySearch(arr,num):
        print(1)
    else:
        print(0)