import heapq

n = 50000
times =[5,7,10,100,20,301,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
new_times = []

for i in range(len(times)):
    heapq.heappush(new_times,(times[i],times[i]))
    
while n>0:
    current_time,interval=heapq.heappop(new_times)
    n-=1
    answer = current_time
    current_time += interval
    heapq.heappush(new_times,(current_time,interval))
print(answer)