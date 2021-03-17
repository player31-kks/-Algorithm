N,K = map(int,input().split())
numbers = [i+1 for i in range(N)]

res = []
point = 0
count = 1

while any(numbers):
    if numbers[point]!=0 and count==K:
        res.append(str(numbers[point]))
        numbers[point] = 0
        count = 1
    elif numbers[point]!=0:
        count+=1
    point = (point+1)%(N)

result = ", ".join(res)
print(f'<{result}>')