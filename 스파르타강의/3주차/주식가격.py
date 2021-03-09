stack =[]
answer = [0]*len(prices)
for idx,price in enumerate(prices):
    while stack and stack[-1][1] > price:
        i,v=stack.pop()
        answer[i] = idx-i 
    stack.append((idx,price))
    
while stack:
    i,v=stack.pop()
    answer[i] = len(answer)-1-i
print(answer)