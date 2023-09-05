a,b,c = map(int,input().split())

count  = [0]*101
for _ in range(3):
    start,end = map(int,input().split())
    for i in range(start,end):
        count[i]+=1

res = 0
def build_price(value):
    score = [0,a,b,c]
    return score[value]*value
print(sum(map(build_price,count)))


