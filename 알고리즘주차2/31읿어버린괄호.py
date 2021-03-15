expression = input()

add_expressions=expression.split('-')
nums = []
for add_expression in add_expressions:
    if '+' in add_expression:
        add_num=list(map(int,add_expression.split("+")))
        nums.append(sum(add_num))
    else:
        nums.append(int(add_expression))
        
result = 0
for idx,num in enumerate(nums):
    if idx==0:
        result+=num
    else:
        result-=num
print(result)