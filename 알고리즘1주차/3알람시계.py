
# 음수를 나머지연산을 할 때
# 범위가 정해지면 나머지 연산으로 풀어라!!
H,M = map(int,input().split())
if M-45<0:
    H = (H-1)%24 #0~23 
M = (M-45)%60
print(H,M)
print(-1%24) # 23
