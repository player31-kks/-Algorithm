N = int(input())
numbers = list(map(int,input().split()))

res =[]
accum = 0
for idx,num in enumerate(numbers):
    origin=num*(idx+1)-accum
    res.append(str(origin))
    accum+=origin

print(" ".join(res))