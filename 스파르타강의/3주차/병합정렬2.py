array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    left_value = merge_sort(array[:mid])
    right_value = merge_sort(array[mid:])
    return merge(left_value,right_value)


def merge(array1, array2):
    a1 = 0
    a2 = 0
    new_arr =[]
    while a1<len(array1) and a2<len(array2):
        if array1[a1] <= array2[a2]:
            new_arr.append(array1[a1])
            a1+=1
        else:
            new_arr.append(array2[a2])
            a2+=1
    if a1>a2:
        new_arr+=array2[a2:]
    else:
        new_arr+=array1[a1:]
    return new_arr


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!