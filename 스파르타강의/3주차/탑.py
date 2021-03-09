top_height=[6, 9, 5, 7, 4]
top_height.reverse()

stack = []
res = []
# 4 7 5 9 6 
for idx,value in enumerate(top_height):
    while stack and stack[-1][1] <value:
        i,v=stack.pop()
        res.append(len(top_height)-idx)    
    stack.append((idx,value))
while stack:
    stack.pop()
    res.append(0)
res.reverse()
print(res)

    

