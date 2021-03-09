numbers = [1, 1, 1, 1, 1]
target_number = 3

count = 0
def DFS(array,total,depth):
    global count
    if depth >len(numbers)-1:
        if total == target_number:
            count+=1   
        return
    DFS(array,total+array[depth],depth+1)
    DFS(array,total-array[depth],depth+1)
DFS(numbers,0,0)
print(count)