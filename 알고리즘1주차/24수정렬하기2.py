import heapq  # python에서 heap을 사용하기 위한 라이브러리
import sys    # python에서는 min heap을 지원한다. 
N = int(input())
arr =[]

for _ in range(N):
    num=int(sys.stdin.readline())
    heapq.heappush(arr,num)  # arr를 heap으로 이용
for _ in range(N):
    print(heapq.heappop(arr)) # heap에서 pop


