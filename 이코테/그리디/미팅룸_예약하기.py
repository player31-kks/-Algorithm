import heapq
meetings = [[12,16],[9,11],[10,14],[9,12],[13,16],[15,17]]

# 우선순위 큐를 이용할 때는 heapq를 이용하자
# 겹치는 것은 그림으로 표현해보자 end - start일때가 많다

meetings.sort(key = lambda x:x[0])
queue = [float('inf')]
room = 0
for meeting in meetings:
  start,end = meeting
  if queue and queue[0] > start:
    room+=1
  else:
    heapq.heappop(queue)
  heapq.heappush(queue,end)
print(room)
    
  
  
  
  
  