# 문자열과 weight one point 방식으로 지정한다.
# 문제 : string s와 i번째 문자를 지우기 위한 cost[i]가 주어진다. 연속되는 알파벳을 지우기 위한 최소비용은 몇인가?
s = 'bbbaaac'
weight =[3,1,2,1,5,3,2]

current_char = '.'
current_max_weight =float('-inf')

res = 0
for idx,char in enumerate(s):
  if char!=current_char:
    current_char = char
    current_max_weight = weight[idx]
    continue
    
  if current_max_weight<weight[idx]:
    res+=current_max_weight
    current_max_weight = weight[idx]
  else:
    res+=weight[idx]
print(res)
