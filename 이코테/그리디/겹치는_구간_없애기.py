intervals = [[1,2],[2,3],[3,4],[1,3]]
# 끝나는 지점으로 sorting을 해야지 남아있는 공간이 많다.
intervals.sort(key=lambda x :x[1])

current_end =intervals[0][0]
res = 0
for interval in intervals:
  start,end = interval
  #겹치면
  if current_end > start:
    res+=1
  else:
    current_end = end
print(res)