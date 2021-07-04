from collections import defaultdict
import sys
sys.stdin = open('a.txt','rt')

N,M = map(int,input().split())

girlGoup =defaultdict(list)
for _ in range(N):
    girlGoup_name = input()
    girlGoup_num = int(input())
    
    for _ in range(girlGoup_num):
        member_name = input()
        girlGoup[girlGoup_name].append(member_name)


for _ in range(M):
    que = input()
    num =  int(input())
    if num==1:
        for group in girlGoup:
            if que in girlGoup[group]:
                print(group)
                break
    if num==0:
        girlGoup[que].sort()
        for member in girlGoup[que]:
            print(member)