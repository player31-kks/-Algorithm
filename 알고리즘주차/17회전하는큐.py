#19조 금교석

from collections import deque
N,M = map(int,input().split())
numbers = list(map(int,input().split()))
queue = deque([i+1 for i in range(N)])

## deque를 이용하면 rotate하는 것이 쉬워집니다. 
## deque.rotate(양수) => 오른쪽으로 수만큼 이동
## deque.rotate(음수) => 왼쪽으로   수만큼 이동

count = 0
for num in numbers:
    num_idx=queue.index(num)
    front = num_idx  # 찾는 값의 앞에서 부터의 index
    tail = len(queue)-num_idx-1 #찾는 값의 뒤에서 부터의 index
    
    if front > tail: # 앞이 더 크다면 뒤에서 부터 돌리는 것이 이득
        queue.rotate(tail+1) #뒤에서 돌릴 때는 맨앞으로 와야하기 때문에 한번더 rotate한다.
        count+=tail+1
    else:
        queue.rotate(-front) # 뒤로 돌리는 코드
        count+=front
    queue.popleft()
print(count)