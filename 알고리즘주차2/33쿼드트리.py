# import sys
# sys.stdin = open('b.txt','rt')


# def print2D(arr2D):
#     for row in range(len(arr2D)):
#         for col in range(len(arr2D[0])):
#             print(arr2D[row][col],end=" ")
#         print()
#     print()

def is_same_color(arr2D):
    target = arr2D[0][0]
    for row in range(len(arr2D)):
        for col in range(len(arr2D[0])):
            if target != arr2D[row][col]:
                return False
    return True

def split_col_half(arr2D,direction):
    half_2D_arr =[]
    mid = len(arr2D[0])//2
    if direction=="left":
        for row in arr2D:
            half_2D_arr.append(row[:mid])
    elif direction=="right":
        for row in arr2D:
            half_2D_arr.append(row[mid:])
    return half_2D_arr


result = ""
def compression_binaryImage(arr2D):
    global result
    #종료조건
    if is_same_color(arr2D):
        target = arr2D[0][0]
        result+=f'{target}'
        return

    mid = len(arr2D)//2
    result +='('
    compression_binaryImage(split_col_half(arr2D[:mid],"left"))
    compression_binaryImage(split_col_half(arr2D[:mid],"right"))
    compression_binaryImage(split_col_half(arr2D[mid:],"left"))
    compression_binaryImage(split_col_half(arr2D[mid:],"right"))
    result +=')'

N = int(input())
image =[]
for _ in range(N):
    row=list(input())
    image.append(row)
compression_binaryImage(image,1)
print(f'{result}')