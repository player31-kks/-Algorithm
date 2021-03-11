from collections import deque

N = int(input())
stack =[]
queue = deque([i+1 for i in range(N)])
res =[]
for _ in range(N):
    num=int(input())
    while stack or queue:
        if stack and stack[-1]==num:
            stack.pop()
            res.append("-")
            break
        if queue:
            queue_num = queue.popleft()
            stack.append(queue_num)
            res.append("+")
        else:
            print("NO")
            exit(0)
            
print("\n".join(res))