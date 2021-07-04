inputs ="acacdfehdehjkj"

size = len(inputs)
check =[0 for i in range(size)]
left,right = 0,size-1
partition = 0

while left < size:
  if check[left]==1:
    left+=1
    continue
  
  for idx in range(size-1,-1,-1):
    if inputs[left] == inputs[idx]:
      break
    
  if left==right and check[right]==1:
    partition+=1
    
  left+=1
  check[right]=1
  right = size-1
  print(left)
print(partition)