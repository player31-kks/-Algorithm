
def merge(arr1,arr2):
    new_arr = []
    arr1_idx = 0;arr2_idx=0
    while arr1_idx<len(arr1) and arr2_idx<len(arr2):
        a1 = arr1[arr1_idx]
        a2 = arr2[arr2_idx]
        if a1[1]== a2[1]:
            if a1[0] < a2[0]:
                new_arr.append(a1)
                arr1_idx+=1
            else:
                new_arr.append(a2)
                arr2_idx+=1
        elif a1[1] < a2[1]:
            new_arr.append(a1)
            arr1_idx+=1
        else:
            new_arr.append(a2)
            arr2_idx+=1
            
    if arr2_idx > arr1_idx:
        new_arr += arr1[arr1_idx:]
    else:
        new_arr += arr2[arr2_idx:]
    return new_arr
        
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)


N = int(input())
coords =[]
for _ in range(N):
    coord = list(map(int,input().split()))
    coords.append(coord)
    
coords=mergeSort(coords)
print(coords)