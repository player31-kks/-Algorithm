import math

a,b,v = map(int,input().split())
h =math.ceil((v-a)/(a-b))+1
print(h)

