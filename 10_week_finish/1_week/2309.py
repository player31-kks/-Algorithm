import copy
heights = [int(input()) for _ in range(9)]
heights.sort()


result =[]
def DFS(start,end,person):
    if start > end or len(person)==7:
        if len(person)==7 and sum(person)==100:
            result.append(copy.deepcopy(person))
            return 
    
    for i in range(start,end):
        person.append(heights[i])
        DFS(i+1,end,person)
        person.pop()


DFS(0,9,[]) 
for person in result[0]:
    print(person)



