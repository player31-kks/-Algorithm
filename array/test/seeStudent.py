input1 = int(input())
nums = list(map(int,input().split()))

stack = []
for num in nums:
    if not stack:
        stack.append(num)
    if stack and stack[-1] < num:
        stack.append(num)

print(len(stack))