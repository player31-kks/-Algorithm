from collections import deque
N = int(input())
numbers = list(map(int,input().split()))
numbers.sort(reverse=True)

queue = deque(numbers)
count = 0
while queue:
    cnt = queue[0]
    for _ in range(cnt):
        queue.popleft()
    count+=1
print(count)
        
