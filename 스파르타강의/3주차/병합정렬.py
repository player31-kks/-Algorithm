array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


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


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!