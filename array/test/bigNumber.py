input1 = int(input())
nums = list(map(int,input().split()))

ex_num = nums[0]
result = [ex_num]

for num in nums:
    if ex_num < num:
        result.append(num)
    ex_num = num

for num in result:
    print(num, end=" ")