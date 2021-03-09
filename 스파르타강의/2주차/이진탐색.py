def binarySearch(arr,value):
    left = 0
    right = len(arr)-1
    
    while left<=right:
        pivot = int((left+right)/2)
        if arr[pivot] == value:
            return True
        elif arr[pivot] > value:
            right = pivot-1
        else:
            left = pivot+1
    else:
        return False
    
    
arr =[i for i in range(1,100)]
print(binarySearch(arr,99))