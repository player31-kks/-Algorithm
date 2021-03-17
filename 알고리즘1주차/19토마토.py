from collections import deque
# import sys
# sys.stdin = open('a.txt','rt')

def BFS(tomato):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    queue = deque(tomato)
    
    while queue:
        row,col,day = queue.popleft()
        for i in range(4):
            new_row = row+dr[i]
            new_col = col+dc[i]
            if 0<=new_row<N and 0<=new_col<M and MAP[new_row][new_col]==0:
                MAP[new_row][new_col] = 1
                queue.append((new_row,new_col,day+1))
    return day
    
#초기화
M,N = map(int,input().split())
MAP =[]
for _ in range(N):
    row = list(map(int,input().split()))
    MAP.append(row)


    
# 1만 찾아서 넣기
tomato =[]
for row in range(len(MAP)):
    for col in range(len(MAP[0])):
        if MAP[row][col]==1:
            tomato.append((row,col,0))
# 최대날짜 찾기
day=BFS(tomato)
# 최종검사
for row in range(len(MAP)):
    for col in range(len(MAP[0])):
        if MAP[row][col]==0:
            print("-1")
            exit(0)
print(day)
        