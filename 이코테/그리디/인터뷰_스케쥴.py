# 둘 사이의 간격을 먼저 봐라!!
# 글로벌 하게 생각하면 먼 산으로 가게 되어있다.


costs = [[10,20],[30,200],[400,50],[30,20]]
boundary = len(costs)//2
costs.sort(key=lambda x : -(x[1]-x[0]))
res = 0;flag = 0

for idx,cost in enumerate(costs):
  if idx >= boundary:
    flag = 1
  res+=cost[flag]
print(res)
