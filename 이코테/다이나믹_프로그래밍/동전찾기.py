coins = [2,3,5]
target = 11

dp = [0,-1,1,1]

for i in range(4,target+1):
  tempt = []
  for j in range(3):
      if i-j<0:
        continue
      tempt.append(dp[i-coins[j]])
  min_value = min([i for i in tempt if i>=0])+1
  dp.append(min_value)
print(dp[target])

  