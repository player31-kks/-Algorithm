import sys
from itertools import combinations

sys.stdin = open('a.txt','rt')

N = int(input())
Garden = []
MAP = [[0]*N for i in range(N)] 


def is_valid(val):
    points = []
    for i in range(3):
        points.append((val[i][1],val[i][2]))
    
    res = []
    for point in points:
        for i in range(5):
            new_row = point[0]+dr[i]
            new_col = point[1]+dc[i]
            
            if (new_row,new_col) in res:
                return False
            else:
                res.append((new_row,new_col))
    return True
        
        
    
dr = [1,0,-1,0,0]
dc = [0,1,0,-1,0]

for i in range(N):
    row = list(map(int,input().split()))
    Garden.append(row)
    
prices = []
for row in range(1,N-1):
    for col in range(1,N-1):
        for idx in range(5):
            new_row = row+dr[idx]
            new_col = col+dc[idx]
            MAP[row][col]+=Garden[new_row][new_col]
        prices.append((MAP[row][col],row,col))

prices.sort()

min_num = int(1e9)
for val in combinations(prices,3):
    s = 0
    for i in range(3):
        s+= val[i][0]
    if min_num > s and is_valid(val):
        min_num = min(min_num,s)
    else:
        continue
print(min_num)
        